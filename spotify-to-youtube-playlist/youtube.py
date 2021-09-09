import requests
import json
import urllib.parse


def get_video_ids_from_track_names(track_names: list):
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


def get_video_ids_from_track_names_without_api(track_names: list):
    """Retrieve the video ids from the songs for which the names are given in the input list.
    This approach does not use the YouTube API. The YouTube API has a limit on requests per day which is quite low.

    Args:
        track_names (list): list containing string with the song titles and artist names

    Returns:
        list: list containing the video ids for the songs for which the names are given in the input list
    """
    prefix = '"videoId":"'  # Prefix to search in server response

    video_ids = []

    for tn in track_names:
        query = urllib.parse.quote_plus(tn)
        response = requests.get(
            f'https://www.youtube.com/results?search_query={query}')
        raw_body_str = response.text
        cut = raw_body_str.split(prefix)[1]
        video_ids.append(cut.split('"')[0])

    return video_ids


def add_videos_to_playlist():
    pass
    # Too difficult if not using the API
