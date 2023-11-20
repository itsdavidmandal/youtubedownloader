from pytube import YouTube
import os

def download_youtube_video(video_url, download_folder):
    try:
        # Accessing the YouTube video
        yt = YouTube(video_url)

        # Choose the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Create the download directory if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Download the video to the specified folder
        print("Downloading...")
        video_stream.download(output_path=download_folder, filename='downloaded_video')

        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'youtube_video_url' with the URL of the YouTube video you want to download
ytlink = input(str(" Enter the Video's link :"))
video_url = ytlink

# Replace 'your_download_folder' with the desired folder path to save the video
folder_path= input(str(" Copy the folder's path : "))

download_folder = folder_path

download_youtube_video(video_url, download_folder)
