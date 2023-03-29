# YouTube Playlist Downloader

This repository contains a simple implementation of a YouTube playlist downloader using the Google API and `pytube`. Although `pytube` already has the capability to download playlists, this implementation was created for fun and learning purposes.

## Files and Functions

### 1. playlist.py

This file contains the `get_title()` function, which takes a `playlist_url` and `API_KEY` as input and returns the title of the YouTube playlist.

#### Usage:

```python
from playlist import get_title
title = get_title(playlist_url='your_playlist_url_here', API_KEY='your_api_key_here')
```

### 2. playlistItems.py

This file contains the `get_playlistItems_url()` function, which takes a `playlist_url` and `API_KEY` as input and returns a list of URLs for the videos in the playlist.

#### Usage:

```python
from playlistItems import get_playlistItems_url
video_urls = get_playlistItems_url(playlist_url='your_playlist_url_here')
```
### 3. download.py

This file contains the `download()` function, which takes a list of video URLs (`videos`), the desired video resolution (`res`), a download folder name (`download_folder`, default is the current datetime), and a flag indicating whether to download only the video (`only_video`, default is `True`). It downloads the videos from the list into the specified folder.

#### Usage:

```python
from download import download
video_urls = ['https://www.youtube.com/watch?v=example1', 'https://www.youtube.com/watch?v=example2']
download(videos=video_urls, res='720p', download_folder='MyPlaylist', only_video=True)
```

### 4. main.py (Updated)

This file contains the `run()` function, which takes a `playlist_url`, `API_KEY`, and the desired video resolution (`res`) as input. It gets the playlist title and video URLs, and downloads the videos from the playlist into a folder named with the playlist title.

#### Usage:

```python
from main import run
```
Refer to the [YouTube Data API v3](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html) for more information. 
