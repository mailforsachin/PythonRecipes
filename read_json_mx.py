import json
import config
import sqlite3
import os
import glob

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (TypeError, ValueError) as e:
        print(f"Error reading {file_path}: {e}")

def extract_nested_values(data):
    track_details = []
    playlists = data.get('playlists', [])

    for playlist in playlists:
        tracks = playlist.get('tracks', [])
        for track in tracks:
            details = {
                'artist_name': track.get('artist_name'),
                'track_name': track.get('track_name'),
                'album_name': track.get('album_name'),
                'artist_uri': track.get('artist_uri'),
                'album_uri': track.get('album_uri'),
                'track_uri': track.get('track_uri')
            }
            track_details.append(details)

    return track_details

def insert_track_details_into_db(track_details):
    if track_details:
        conn = sqlite3.connect(config.DATABASE_LOCATION)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Spotify_Offline_Db_Complete (
                artist_name TEXT NOT NULL,
                artist_uri TEXT NOT NULL,
                track_name TEXT NOT NULL,
                track_uri  TEXT NOT NULL,
                album_name TEXT NOT NULL,
                album_uri TEXT NOT NULL
            )
        ''')

        for detail in track_details:
            cursor.execute('''
                INSERT INTO Spotify_Offline_Db_Complete (artist_name, artist_uri, track_name, track_uri, album_name, album_uri)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                detail['artist_name'], 
                detail['artist_uri'], 
                detail['track_name'], 
                detail['track_uri'], 
                detail['album_name'], 
                detail['album_uri']
            ))

        conn.commit()
        conn.close()

if __name__ == "__main__":
    folder_path = config.JSON_FOLDER_PATH  # Update your config to include the folder path
    json_files = glob.glob(os.path.join(folder_path, "*.json"))

    for json_file in json_files:
        print(f"Processing file: {json_file}")
        data = read_json_file(json_file)
        if data:
            track_details = extract_nested_values(data)
            insert_track_details_into_db(track_details)
