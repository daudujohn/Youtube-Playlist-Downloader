from pytube import YouTube, exceptions
from datetime import datetime
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download(videos: list, res: str, download_folder = str(datetime.now()), only_video = True):

    if type(videos) != list:
        videos = [videos]
    if videos == []:
        return 'List of videos is empty'
    for video in videos:
        try:
            yt = YouTube(video)
            stream = yt.streams.filter(res=res, only_video=only_video).first()
            # print(yt.streams.filter(only_video=True).all())
            if stream is not None:
                stream.download(f'./downloads/{download_folder}')
            else:
                yt.streams.get_highest_resolution().download(f'./downloads/{download_folder}')
            print('downloading...')
        except TypeError:
            return 'youtube link should be a valid string'
        except exceptions.VideoUnavailable:
            return 'Invalid youtube url'
        except exceptions.RegexMatchError:
            return 'Invalid youtube url'
        except AttributeError:
            return 'Invalid Resolution input'