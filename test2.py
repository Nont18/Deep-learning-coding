import requests
from bs4 import BeautifulSoup

# Initial index
index = 54459

# Base URL
base_url = 'https://www.th-sl.com/?p='

for i in range(10):
    index -= 1
    full_url = base_url + str(index)
    print(f"Fetching URL: {full_url}")

    # Send a GET request to the URL
    r = requests.get(full_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Print the page title for debugging purposes
    print(f"Page title: {soup.title.string if soup.title else 'No title'}")

    # Check if the page contains a video tag
    video_tag = soup.find('video')
    if video_tag:
        video_url = video_tag.get('src')
        if video_url:
            print(f"Video found: {video_url}")

            # Download the video
            video_response = requests.get(video_url)
            video_filename = f'video_{index}.mp4'
            with open(video_filename, 'wb') as file:
                file.write(video_response.content)
            
            print(f"Video downloaded successfully as {video_filename}")
    else:
        print("No video found on this page")
