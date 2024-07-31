#ALTER TABLE Distinct_Album_URI ADD COLUMN is_processed BOOLEAN DEFAULT 0;
import sqlite3
import requests
import json
import base64
import time
import os
import config

# Get access token from Spotify
def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{config.CLIENT_ID}:{config.CLIENT_SECRET}".encode()).decode()
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Could not authenticate, please check your client credentials")
    return response.json()['access_token']

# Fetch album details from Spotify with incremental backoff
def get_album_data(token, album_uris, max_retries=5):
    base_url = "https://api.spotify.com/v1/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{base_url}?ids={','.join(album_uris)}"
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 3600))
            print(f"Rate limited by Spotify API. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
        else:
            print(f"Failed to get album data: {response.status_code}. Retrying in {2 ** attempt} seconds...")
            time.sleep(2 ** attempt)
    raise Exception(f"Failed to retrieve album data after {max_retries} attempts")

# Fetch album URIs from SQLite database in chunks of 20
def fetch_album_uris_from_db(db_path, batch_size=20):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT album_uri FROM Distinct_Album_URI WHERE is_processed = 0")
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        # Remove "spotify:album:" prefix
        album_uris = [row[0].replace('spotify:album:', '') for row in rows]
        yield album_uris
    conn.close()

# Save album data to a JSON file
def save_json(data, filename):
    output_dir = "C:\\Users\\sachi\\OneDrive\\Code\\PythonRecipes\\SpotifyAlbum\\"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data successfully saved to {filename}")

# Handle retries for SQLite operations
def execute_with_retries(func, *args, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func(*args)
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                print(f"Database is locked. Retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)
            else:
                raise
    raise Exception("Failed to execute database operation after maximum retries")

# Main function to run the script
def main():
    token = get_token()
    output_dir = "C:\\Users\\sachi\\OneDrive\\Code\\PythonRecipes\\SpotifyAlbum\\"

    conn = sqlite3.connect(config.DATABASE_LOCATION)
    cursor = conn.cursor()

    for album_batch in fetch_album_uris_from_db(config.DATABASE_LOCATION):
        print(f"Fetching data for albums: {album_batch}")
        album_data = get_album_data(token, album_batch)

        if 'albums' in album_data:
            for album in album_data['albums']:
                if album is not None:
                    try:
                        album_id = album['id']
                        filename = f"{album_id}_album.json"
                        filepath = os.path.join(output_dir, filename)

                        # Check if file already exists
                        if os.path.exists(filepath):
                            print(f"File {filename} already exists. Skipping.")
                            continue

                        # Save the album data if file does not exist
                        save_json(album, filename)
                        
                    except KeyError:
                        print(f"Error finding 'id' in album data: {album}")
                        continue
                else:
                    print(f"Album data is None for batch: {album_batch}")
                    continue
        else:
            print(f"No albums key found in response: {album_data}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()