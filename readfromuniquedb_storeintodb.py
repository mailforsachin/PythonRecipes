import os
import config
import sqlite3

# Path to the SQLite database file
db_path = config.DATABASE_LOCATION  # Replace with your actual database path

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the new table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS unique_albums (
        artist_name TEXT,
        artist_uri TEXT,
        track_name TEXT,
        track_uri TEXT,
        album_name TEXT,
        album_uri TEXT
    )
''')

# Fetch the data from the original table
cursor.execute('''
    SELECT artist_name, artist_uri, track_name, track_uri, album_name, album_uri
    FROM Spotify_Offline_Db_UniqueSongs
''')
rows = cursor.fetchall()

# Process each row and check for album file existence
for row in rows:
    artist_name, artist_uri, track_name, track_uri, album_name, album_uri = row
    
    # Extract the album ID from album_uri by removing 'spotify:album:'
    album_id = album_uri.replace('spotify:album:', '')
    #print(album_id)
    # Check if a file with the album ID as part of its name exists
    files_in_directory = os.listdir(config.CHECK_DIR)
    if any(album_id in filename for filename in files_in_directory):
        #print (files_in_directory);
        # If no such file exists, insert the record into unique_albums table
        cursor.execute('''
            INSERT INTO unique_albums (artist_name, artist_uri, track_name, track_uri, album_name, album_uri)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (artist_name, artist_uri, track_name, track_uri, album_name, album_uri))

# Commit the transaction and close the connection
conn.commit()
conn.close()