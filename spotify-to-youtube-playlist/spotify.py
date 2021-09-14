import requests
import json
import base64


def get_access_token() -> str:
    """Retrieve the access token needed for communicating with the Spotify API.
    The client-id and the client-secret from the config.json file are used for this (also see README).
    More information about this process can be found here: https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow.

    Returns:
        string: Spotify API access token
    """
    with open('config.json', 'r') as config_file:
        conf = json.load(config_file)
        client_id = conf['spotify']['client_id']
        client_secret = conf['spotify']['client_secret']
    auth = f'{client_id}:{client_secret}'
    auth_bytes = auth.encode('ascii')
    auth_base64_bytes = base64.b64encode(auth_bytes)
    auth_base64 = auth_base64_bytes.decode('ascii')

    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data="grant_type=client_credentials",
        headers=headers
    )
    return json.loads(response.content)['access_token']


def get_track_names_from_playlist(playlist_id: str) -> list:
    """Get the titles and artists for all the songs for the Spotify playlist with the given id.
    More information can be found here: https://developer.spotify.com/console/get-playlist/

    Args:
        playlist_id (string): id of the Spotify playlist

    Returns:
        list: list containing the track names of all the songs in the Spotify playlist with the given id
    """
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    token = get_access_token()

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    playlist_response = requests.get(playlist_url, headers=headers)

    response_json = json.loads(playlist_response.content)
    tracks_json: list = response_json['items']

    # Spotify only returns the first 100 tracks of a playlist, so we can iterate with an offset, see https://developer.spotify.com/console/get-current-user-playlists/
    offset_counter = 1
    while len(response_json['items']) >= 100 and offset_counter < 4:
        playlist_url_offset = playlist_url + \
            '?offset=' + str(offset_counter*100)
        response_json = json.loads(requests.get(
            playlist_url_offset, headers=headers).content)
        tracks_json.extend(response_json['items'])
        offset_counter += 1

    tracks = []

    for t in tracks_json:
        track_name = t['track']['name']
        track_artists = []
        for a in t['track']['artists']:
            track_artists.append(a['name'])
        track_artists_joined = ', '.join(track_artists)
        tracks.append(f'{track_name} - {track_artists_joined}')

    return tracks
