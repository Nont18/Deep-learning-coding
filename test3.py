import requests

# Replace this URL with the URL of the blob video you want to download
url = 'https://dic.ttrs.or.th/0597f773-cfe7-4b7c-b30b-7bc0512583aa'

# Specify the filename and path where you want to save the video
output_file = 'video.gif'

# Send a GET request to the URL
response = requests.get(url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Open the output file in write-binary mode
    with open(output_file, 'wb') as file:
        # Write the response content to the file in chunks
        for chunk in response.iter_content(chunk_size=3500):
            file.write(chunk)
    print(f"Video successfully downloaded to {output_file}")
else:
    print(f"Failed to download video. HTTP Status Code: {response.status_code}")
