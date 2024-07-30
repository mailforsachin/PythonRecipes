import json
import config
import sqlite3


def read_json_file(my_json_file):
    try:
        with open(my_json_file, 'r') as file:
            data = json.load(file)
            return data
    except TypeError:
        print("Type is incorrect!")
    except ValueError:
        print("Value is incorrect")

def extract_nested_values(data):
    track_details = []
    playlists = data.get('playlists', [])
    
    for playlist in playlists:
        tracks = playlist.get('tracks', [])
        for track in tracks:
            details = {
                'artist_name': track.get('artist_name'),
                'track_name': track.get('track_name'),
                'album_name': track.get('album_name')
            }
            track_details.append(details)
    
    return track_details

my_json_file = config.JSON_FILE_PATH

data = read_json_file(my_json_file);
#print(data)
if data:
   
    track_details = extract_nested_values(data)

    if track_details:
        #print("Extracted Album Names:")
        for detail in track_details:
                #print(f"Artist: {detail['artist_name']}, Track: {detail['track_name']}, Album: {detail['album_name']}")
                conn=sqlite3.connect(config.DATABASE_LOCATION)
                cursor=conn.cursor();
                #cursor.execute('''drop table Spotify_Offline_Db''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Spotify_Offline_Db (
                        artist_name TEXT NOT NULL,
                        track_name TEXT NOT NULL,
                        album_name TEXT NOT NULL
                    )
                ''')
                cursor.execute('''INSERT INTO Spotify_Offline_Db (artist_name, track_name, album_name)
                      VALUES (?, ?, ?)''', (detail['artist_name'], detail['track_name'], detail['album_name']))
                conn.commit()
                conn.close()