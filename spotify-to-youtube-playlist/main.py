from spotify import get_track_names_from_playlist
from youtube import get_video_ids_from_track_names, get_video_ids_from_track_names_without_api

playlist_id = '4bOzSOi1cOpuTpXAa0j2JJ'

tracks = get_track_names_from_playlist(playlist_id)

# print(get_video_ids_from_track_names(tracks))
print(get_video_ids_from_track_names_without_api(tracks))
