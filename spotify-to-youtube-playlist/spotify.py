import requests
import json


def get_track_names_from_playlist(playlist_id: str):
    """Get the titles and artists for all the songs for the Spotify playlist with the given id

    Args:
        playlist_id (string): id of the Spotify playlist

    Returns:
        list: list containing the track names of all the songs in the Spotify playlist with the given id
    """
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'

    with open('config.json', 'r') as file:
        conf = json.load(file)
        token = conf['spotify']['token']

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    playlist_response = requests.get(playlist_url, headers=headers)

    response_json = json.loads(playlist_response.content)
    tracks_json = response_json['tracks']['items']
    tracks = []

    for t in tracks_json:
        track_name = t['track']['name']
        track_artists = []
        for a in t['track']['artists']:
            track_artists.append(a['name'])
        track_artists_joined = ', '.join(track_artists)
        tracks.append(f'{track_name} - {track_artists_joined}')

    return tracks
