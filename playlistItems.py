import google.auth
from googleapiclient.discovery import build

def get_playlistItems_url(playlist_url: str, API_KEY) -> list:

    credentials, project = google.auth.default()
    youtube = build('youtube', 'v3', credentials=credentials)

    VIDEO_STUB = 'https://www.youtube.com/watch?v='
    videos_in_playlist = []

    playlistitems_list_request = youtube.playlistItems().list(
        part = 'snippet', 
        playlistId = playlist_url.split('?list=')[1], 
        maxResults = 50
    )

    playlistitems_list_response = playlistitems_list_request.execute()

    for item in playlistitems_list_response['items']: 
        videoId = item['snippet']['resourceId']['videoId']
        videos_in_playlist.append(VIDEO_STUB + videoId)


    while 'nextPageToken' in playlistitems_list_response:
        next_page_token = playlistitems_list_response['nextPageToken']
        playlistitems_list_request = youtube.playlistItems().list(
            part = 'snippet', 
            pageToken = next_page_token, 
            maxResults = 50,
            playlistId = playlist_url.split('?list=')[1], 
        )

        playlistitems_list_response = playlistitems_list_request.execute()
        for item in playlistitems_list_response['items']: 
            videoId = item['snippet']['resourceId']['videoId']
            videos_in_playlist.append(VIDEO_STUB + videoId)

    return videos_in_playlist