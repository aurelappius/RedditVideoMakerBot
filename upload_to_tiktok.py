import os
import shutil
from tiktok_uploader.upload import upload_video

# Directories
VIDEO_DIR = 'results'
UPLOADED_DIR = 'uploaded'
COOKIES_FILE = 'cookies.txt'

# Ensure the uploaded directory exists
os.makedirs(UPLOADED_DIR, exist_ok=True)


def upload_and_move(video_path):
    """
    Uploads a video to TikTok and moves it to the 'uploaded' directory upon success.
    """
    try:
        # Upload video
        upload_video(
            video_path, description='Your video description', cookies=COOKIES_FILE)
        print(f'Successfully uploaded: {video_path}')

        # Move video to 'uploaded' directory
        destination = os.path.join(UPLOADED_DIR, os.path.basename(video_path))
        shutil.move(video_path, destination)
        print(f'Moved to uploaded folder: {destination}')

    except Exception as e:
        print(f'Failed to upload {video_path}: {e}')


def scan_and_upload_videos():
    """
    Scans the VIDEO_DIR and its subdirectories for videos and uploads them.
    """
    for root, _, files in os.walk(VIDEO_DIR):
        for file in files:
            if file.lower().endswith(('.mp4', '.mov', '.avi')):  # Add other video formats as needed
                video_path = os.path.join(root, file)
                upload_and_move(video_path)


if __name__ == '__main__':
    scan_and_upload_videos()
