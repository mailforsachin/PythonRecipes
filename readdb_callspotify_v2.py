import sqlite3
import requests
import json
import base64
import time
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
    cursor.execute("SELECT album_uri FROM Distinct_Album_URI")
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
    with open("C:\\Users\\sachi\\OneDrive\\Code\\PythonRecipes\\SpotifyAlbum\\" + filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data successfully saved to {filename}")

# Main function to run the script
def main():
    token = get_token()

    for album_batch in fetch_album_uris_from_db(config.DATABASE_LOCATION):
        print(f"Fetching data for albums: {album_batch}")
        album_data = get_album_data(token, album_batch)
        if album_data:
            for album in album_data['albums']:
                album_id = album['id']
                filename = f"{album_id}_album.json"
                save_json(album, filename)
        else:
            print(f"No data found for albums: {album_batch}")

if __name__ == "__main__":
    main()