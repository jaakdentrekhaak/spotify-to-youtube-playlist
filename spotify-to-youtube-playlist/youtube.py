import requests
import json
import urllib.parse


def get_video_ids_from_track_names_with_api(track_names: list) -> list:
    """Retrieve the video ids from the songs for which the names are given in the input list.

    Args:
        track_names (list): list containing string with the song titles and artist names

    Returns:
        list: list containing the video ids for the songs for which the names are given in the input list
    """

    with open('config.json', 'r') as config_file:
        conf = json.load(config_file)
        API_KEY = conf['youtube']['api_key']

    headers = {
        'Accept': 'application/json'
    }

    video_ids = []

    for tn in track_names:

        query = urllib.parse.quote_plus(tn)

        url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&type=video&q={query}&key={API_KEY}'

        response = requests.get(
            url,
            headers=headers
        )
        response_json = json.loads(response.content)

        video_ids.append(response_json['items'][0]['id']['videoId'])

    return video_ids


def progbar(curr, total, full_progbar):
    """Print progress bar. Source: https://geekyisawesome.blogspot.com/2016/07/python-console-progress-bar-using-b-and.html

    Args:
        curr (int): current iteration
        total (int): total iterations
        full_progbar (int): size of the progress bar
    """
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar -
          filled_progbar), '[{:>7.2%}]'.format(frac), end='')
    if curr == total:
        print('\n')


def get_video_ids_from_track_names(track_names: list) -> list:
    """Retrieve the video ids from the songs for which the names are given in the input list.
    This approach does not use the YouTube API. The YouTube API has a limit on requests per day which is quite low.
    This function searches YouTube for the name and artist of a song and searches for the video ID inside an HTML file.

    Args:
        track_names (list): list containing string with the song titles and artist names

    Returns:
        list: list containing the video ids for the songs for which the names are given in the input list
    """
    prefix = '"videoId":"'  # Prefix to search in server response

    video_ids = []

    counter = 1
    for tn in track_names:
        progbar(counter, len(track_names), 20)
        query = urllib.parse.quote_plus(tn)
        response = requests.get(
            f'https://www.youtube.com/results?search_query={query}')
        raw_body_str = response.text
        cut = raw_body_str.split(prefix)[1]
        video_ids.append(cut.split('"')[0])
        counter += 1

    return video_ids


def add_videos_to_playlist(playlist_id: str, video_ids: list, auth: str, cookie: str, key: str) -> int:
    """Add YouTube videos corresponding to the given video ids to a playlist with the given playlist id.

    Args:
        playlist_id (str): ID of a YouTube playlist you want to add videos to (your own playlist)
        video_ids (list): list with IDs of the videos you want to add to the playlist
        auth (str): HTTP header needed for authorization
        cookie (str): HTTP header needed for authorization
        key (str): key needed for authorization

    Returns:
        int: status code for the HTTP request to YouTube
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Content-Type": "application/json",
        "Authorization": auth,
        "Origin": "https://www.youtube.com",
        "Cookie": cookie
    }

    body = {
        'playlistId': playlist_id,
        'actions': [
            {
                'action': 'ACTION_ADD_VIDEO',
                'addedVideoId': v,
                'dedupeOption': 'DEDUPE_OPTION_SKIP'  # Else returns error when duplicate found
            } for v in video_ids
        ]
    }

    context = {
        "context": {
            "client": {
                "clientName": "WEB_REMIX",
                "clientVersion": "0.1",
            },
        }
    }

    body.update(context)

    response = requests.post(f'https://www.youtube.com/youtubei/v1/browse/edit_playlist?key={key}',
                             json=body,
                             headers=headers)

    return response.status_code


def create_playlist(title: str, public: bool, auth: str, cookie: str, key: str) -> str:
    """Create a YouTube playlist with the given title.

    Args:
        title (str): title for the YouTube playlist
        public (bool): whether or not this playlist needs to be public
        auth (str): HTTP header needed for authorization
        cookie (str): HTTP header needed for authorization
        key (str): key needed for authorization

    Returns:
        str: the ID of the created playlist
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Content-Type": "application/json",
        "Authorization": auth,
        "Origin": "https://www.youtube.com",
        "Cookie": cookie
    }

    body = {
        'privacyStatus': 'PUBLIC' if public == True else 'PRIVATE',
        'title': title,
    }

    context = {
        "context": {
            "client": {
                "clientName": "WEB_REMIX",
                "clientVersion": "0.1",
            },
        }
    }

    body.update(context)

    response = requests.post(f'https://www.youtube.com/youtubei/v1/playlist/create?key={key}',
                             json=body,
                             headers=headers)

    return response.json()['playlistId']
