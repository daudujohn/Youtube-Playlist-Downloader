import google.auth
from googleapiclient.discovery import build

def get_title(playlist_url: str, API_KEY) -> str: 

    credentials, project = google.auth.default()
    youtube = build('youtube', 'v3', credentials=credentials)

    playlist_request = youtube.playlists().list(
        part = 'snippet', 
        id = playlist_url.split('?list=')[1], 
    )

    playlist_response = playlist_request.execute()

    return playlist_response['items'][0]['snippet']['title']