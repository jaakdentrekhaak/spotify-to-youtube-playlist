from spotify import get_track_names_from_playlist
from youtube import get_video_ids_from_track_names, add_videos_to_playlist, create_playlist
import json

# Open the settings file
with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

# # Get the track names and artist names for the songs in a Spotify playlist
# print('[INFO] Retrieving track names from Spotify...')
# tracks = get_track_names_from_playlist(settings['Spotify_playlist_id'])

# # Get the YouTube video ids corresponding to the songs in the Spotify playlist
# print('[INFO] Searching YouTube for the track names...')
# video_ids = get_video_ids_from_track_names(tracks)

# # Add the YouTube videos to a playlist
# print('[INFO] Adding videos to your YouTube playlist...')
# status_code = add_videos_to_playlist(
#     settings['YouTube_playlist_id'],
#     video_ids,
#     settings['Authorization'],
#     settings['Cookie'],
#     settings['Key']
# )

# if status_code == 200:
#     print('[INFO] Spotify playlist successfully converted to a YouTube playlist')
# else:
#     print('[INFO] Something went wrong, follow the steps in the README.md file')

print(create_playlist('Emo Trap', True,
      settings['Authorization'], settings['Cookie'], settings['Key']))
