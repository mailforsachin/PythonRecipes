# prepare payload to spotify
# read the album_artist
# download json file

# parse json file and get attributes
# use album_artist to populate some fields
# if you encounter 429, exit script log in database done
# terminate connection

import config
import sqlite3

def fetch_album_artists_from_db(DATABASE_LOCATION):
    conn = sqlite3.connect(DATABASE_LOCATION)
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT album_uri FROM Spotify_Offline_Db_Complete")
    album_artists = [row[0] for row in cursor.fetchall()]


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Distinct_Album_URI (
            album_uri TEXT NOT NULL
        )
    ''')
    for album_uri in album_artists:
        cursor.execute('''
            INSERT INTO Distinct_Album_URI (album_uri)
            VALUES (?)
        ''', (album_uri,))

    conn.commit()
    conn.close()

    return album_artists

def main():
    album_artists = fetch_album_artists_from_db(config.DATABASE_LOCATION)
    #print(album_artists)
    #print(type(album_artists))

if __name__ == "__main__":
    main()
