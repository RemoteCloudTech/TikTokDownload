import json
import os
import argparse
import pyktok as pyk
import shutil

# Function to print all keys in JSON
def print_keys(json_obj, parent_key=''):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            print(full_key)
            print_keys(value, full_key)
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            full_key = f"{parent_key}[{index}]"
            print_keys(item, full_key)

def getVideos(data):
    Activity=data['Activity']
    videos=Activity["Favorite Videos"]
    videos=videos["FavoriteVideoList"]
    return videos

# Function to download videos
def download_videos(videos,output_dir):
    for video in videos:
        print(video)
        video_url = video['Link']

        try:
            # download the video to the current directory
            fileInfo = pyk.save_tiktok(video_url, True, os.path.join(output_dir, 'video_data.csv'), 'chrome', True)
                        
            if(len(output_dir) != 0):
                # Source file path
                src = fileInfo['video_fn']
                # Copy the file
                shutil.move(src, output_dir)
            
        except Exception as e:
            print("Error:", str(e))

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Process some file paths.")

    # Add arguments
    parser.add_argument(
        '--filepath',
        type=str,
        default='user_data_tiktok.json',
        help='Path to the file (default: user_data_tiktok.json)'
    )
    
    parser.add_argument(
        '--outputpath',
        type=str,
        default='',
        help='Path to the file (default: )'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Print the filepath
    print(f"Filepath: {args.filepath}")
    
    pyk.specify_browser('chrome') #browser specification may or may not be necessary depending on your local settings

    output_dir = args.outputpath
    print(output_dir)
    if(len(output_dir) != 0):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
    # Open and read the JSON file
    with open(args.filepath, 'r', encoding='utf-8') as file:
        parsed_data = json.load(file)
        
    # Download the videos
    videos = getVideos(parsed_data)
    download_videos(videos,output_dir)
    

if __name__ == "__main__":
    main()