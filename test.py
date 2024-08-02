import requests
import os

def download_video(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

base_url = "https://www.th-sl.com//wp-content/uploads/2024/06/2567-"
start_index = 1299
end_index = 1300  # Change this to the last file index you want to download

save_directory = "./videos"
os.makedirs(save_directory, exist_ok=True)

for index in range(start_index, end_index + 1):
    video_url = f"{base_url}{index}.gif"
    save_path = os.path.join(save_directory, f"{index}.gif")
    download_video(video_url, save_path)
