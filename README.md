# TikTokDownload
Python software to download videos from TikTok Download Your Data .json file.

This software currently only downloads the FavoriteVideoList but can be modified to access any list of tiktok public video urls.

# TikTok instructions
Go to TikTok on a web browser. Go to [TikTok Settings](https://www.tiktok.com/setting) and select Download your Data.
This will open a page to login, select the data you want to download in JSON format, and request the download.

Wait a day or so for the request to change to a Download button. Clicking this will download a user_data_tiktok.json which will be used as an input file.

# How to use
By default the software will open user_data_tiktok.json. This file matches in format the "FavoriteVideoLists" json content from the Download Your Data request on TikTok.

The user_data_tiktok.json has the following format:
```json
{
  "Activity": {
	"Favorite Videos": {
		"FavoriteVideoList": [
			{"Date":"date_here","Link": "video_url_here"},
			{"Date":"date_2_here","Link": "video_2_url_here"}
			]
		}
	}
}
```

## Installation
# prerequisites
install python3
pip install pyktok

## Running the software
Modify or supply your own user_data_tiktok.json. Two videos are provided in the example data file.
To download videos and metadata to your current directory run:
`python downloadtiktok_embed.py`

The software can also be provided an inputpath (json) and outputpath as arguments.
`python downloadtiktok_embed.py --inputpath=user_data_tiktok.json --outputpath=Downloads`

This will print the following message per valid video
```json
{'Date': '$DATE', 'Link': '$URL'}
```
Saved video
 $URL
to
 $PWD
Saved metadata for video
 $URL
to
 $PWD

The $PWD can be ignored. The software first downloads the video to the current directory, the moves it to the outputpath.

## troubleshooting
The software will attempt to download all links following the Activity -> Favorite Videos -> FavoriteVideoList chain. It will print if the URL is malformed or invalid.
# Example  error print for malformed url
Error: HTTPSConnectionPool(host='safaswww.tiktok.com', port=443): Max retries exceeded with url: /@nostromo117/video/6991887885607734533 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000018A7B111060>: Failed to resolve '    ' ([Errno 11001] getaddrinfo failed)"))

## todo items
-Fix output directory, currently videos are stored to the same directory as the python script is ran.

# Acknowledgements
Yes CoPilot was used to make this.
