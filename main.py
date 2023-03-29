import os
from dotenv import load_dotenv
import playlist
import playlistItems
import download

load_dotenv()

API_KEY = os.getenv('API_KEY')

def run(playlist_url, API_KEY, res):
        PLAYLIST_TITLE = playlist.get_title(
                playlist_url=playlist_url,
                API_KEY=API_KEY
        )

        playlistItems_urls = playlistItems.get_playlistItems_url(
                playlist_url=playlist_url,
                API_KEY=API_KEY
        )

        download.download(playlistItems_urls, res, PLAYLIST_TITLE)

        return 'download complete.'