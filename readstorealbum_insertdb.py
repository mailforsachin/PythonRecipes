'''
INSERT INTO spotify_offline_db_updated (artist_name, artist_uri,track_name, track_uri,album_name, album_uri)
SELECT artist_name, artist_uri,track_name, track_uri,album_name, album_uri
FROM spotify_offline_db_complete
LIMIT 100

'''

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
    album_label = data.get('label', '')  # Assuming 'label' is at the album level

    tracks = data.get('tracks', {}).get('items', [])
    for track in tracks:
        track_popularity = track.get('popularity', 'N/A')  # Assuming popularity is at the track level
        track_release_date = track.get('album', {}).get('release_date', '')  # Assuming release_date at the album level
        for artist in track.get('artists', []):
            details = {
                'artist_name': artist.get('name'),
                'track_name': track.get('name'),
                'album_name': track.get('album', {}).get('name', ''),
                'artist_uri': artist.get('uri'),
                'album_uri': track.get('album', {}).get('uri', ''),
                'track_uri': track.get('uri'),
                'artist_id': artist.get('id'),
                'external_urls_spotify': artist.get('external_urls', {}).get('spotify', ''),
                'popularity': track_popularity,
                'release_date': track_release_date,
                'label': album_label
            }
            track_details.append(details)
    return track_details

def insert_track_details_into_db(track_details):
    if track_details:
        conn = sqlite3.connect(config.DATABASE_LOCATION)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Spotify_Offline_Db_Updated (
                artist_name TEXT NOT NULL,
                artist_uri TEXT NOT NULL,
                track_name TEXT NOT NULL,
                track_uri TEXT NOT NULL,
                album_name TEXT NOT NULL,
                album_uri TEXT NOT NULL,
                artist_id TEXT,
                external_urls_spotify TEXT,
                popularity INTEGER,
                release_date TEXT,
                label TEXT
            )
        ''')

        for detail in track_details:
            cursor.execute('''
                INSERT INTO Spotify_Offline_Db_Updated (
                    artist_name, artist_uri, track_name, track_uri,
                    album_name, album_uri, artist_id, 
                    external_urls_spotify, popularity, release_date, label
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                detail['artist_name'], 
                detail['artist_uri'], 
                detail['track_name'], 
                detail['track_uri'], 
                detail['album_name'], 
                detail['album_uri'],
                detail['artist_id'],
                detail['external_urls_spotify'],
                detail['popularity'],
                detail['release_date'],
                detail['label']
            ))

        conn.commit()
        conn.close()

if __name__ == "__main__":
    folder_path = config.JSON_FOLDER_PATH  
    json_files = glob.glob(os.path.join(folder_path, "*.json"))

    for json_file in json_files:
        print(f"Processing file: {json_file}")
        data = read_json_file(json_file)
        if data:
            track_details = extract_nested_values(data)
            insert_track_details_into_db(track_details)