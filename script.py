import json
import os
import requests
from urllib.parse import urlparse

def download_mp4s(json_file, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Load JSON data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for entry in data:
        replay_url = entry.get("replayUrl")
        if replay_url:
            filename = os.path.join(output_folder, os.path.basename(urlparse(replay_url).path))
            
            print(f"Downloading {replay_url}...")
            response = requests.get(replay_url, stream=True)
            
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Saved to {filename}")
            else:
                print(f"Failed to download {replay_url} (Status code: {response.status_code})")

if __name__ == "__main__":
    json_file = "yes.json"  # Change this to your JSON file path
    output_folder = "downloads"  # Change this to your preferred output folder
    download_mp4s(json_file, output_folder)
