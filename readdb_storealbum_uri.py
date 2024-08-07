# prepare payload to spotify
# read the album_artist
# download json file

# parse json file and get attributes
# use album_artist to populate some fields
# if you encounter 429, exit script log in database done
# terminate connection

import config
import sqlite3
import os

# Fetch album URIs from the database and initialize the Distinct_Album_URI table
def fetch_album_artists_from_db(DATABASE_LOCATION):
    conn = sqlite3.connect(DATABASE_LOCATION)
    cursor = conn.cursor()

    # Fetch unique album URIs from the input table
    cursor.execute("SELECT DISTINCT album_uri FROM Spotify_Offline_Db_Complete")
    album_artists = [row[0] for row in cursor.fetchall()]

    # Create the Distinct_Album_URI table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Distinct_Album_URI (
            album_uri TEXT NOT NULL,
            is_processed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')

    # Insert album URIs into the Distinct_Album_URI table if they do not already exist
    for album_uri in album_artists:
        cursor.execute('''
            INSERT OR IGNORE INTO Distinct_Album_URI (album_uri)
            VALUES (?)
        ''', (album_uri,))

    conn.commit()
    conn.close()

    return album_artists

# Update the is_processed flag for album URIs if the associated files exist
def update_processed_flags(DATABASE_LOCATION, OUTPUT_DIR):
    conn = sqlite3.connect(DATABASE_LOCATION)
    cursor = conn.cursor()

    # Fetch album URIs where is_processed is 0
    cursor.execute("SELECT album_uri FROM Distinct_Album_URI WHERE is_processed = 0")
    album_uris = [row[0] for row in cursor.fetchall()]

    for album_uri in album_uris:
        # Remove "spotify:album:" prefix to get the file name
        filename = f"{album_uri.replace('spotify:album:', '')}_album.json"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Check if file exists
        if os.path.exists(filepath):
            print(f"File {filename} exists. Updating is_processed...")
            cursor.execute('''
                UPDATE Distinct_Album_URI
                SET is_processed = 1
                WHERE album_uri = ?
            ''', (album_uri,))

    conn.commit()
    conn.close()

def main():
    album_artists = fetch_album_artists_from_db(config.DATABASE_LOCATION)
    update_processed_flags(config.DATABASE_LOCATION, config.OUTPUT_DIR)

if __name__ == "__main__":
    main()