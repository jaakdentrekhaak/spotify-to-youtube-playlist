from spotify import get_track_names_from_playlist
from youtube import get_video_ids_from_track_names, add_videos_to_playlist
import json

# Open the settings file
with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

# # Get the track names and artist names for the songs in a Spotify playlist
# tracks = get_track_names_from_playlist(settings['Spotify_playlist_id'])

# # Get the YouTube video ids corresponding to the songs in the Spotify playlist
# video_ids = get_video_ids_from_track_names(tracks)

# # Add the YouTube videos to a playlist
# add_videos_to_playlist(
#     settings['YouTube_playlist_id'],
#     video_ids,
#     settings['Authorization'],
#     settings['Cookie'],
#     settings['Key']
# )

add_videos_to_playlist(
    settings['YouTube_playlist_id'],
    [],
    settings['Authorization'],
    settings['Cookie'],
    settings['Key']
)
