from spotify import get_track_names_from_playlist
from youtube import get_video_ids_from_track_names, add_videos_to_playlist, create_playlist
import json

# Open the settings file
with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

# Get the track names and artist names for the songs in a Spotify playlist
print('[INFO] Retrieving track names from Spotify...')
tracks = get_track_names_from_playlist(settings['Spotify_playlist_id'])

# Get the YouTube video ids corresponding to the songs in the Spotify playlist
print('[INFO] Searching YouTube for the track names...')
video_ids = get_video_ids_from_track_names(tracks)

# video_ids = ['UceaB4D0jpo', 'bPOvxEamtnw', 'xvZqHgFz51I', 'S-sJp1FfG7Q', 'tvTRZJ-4EyI', 'l_lblj8Cq0o', 'nF3gWRhcVYs', 'aWhLuy-DGno', 'njCxj4s7n0A', 'b-jZ0LmE8sk', 'fVnXkRcMtWI', 'JSoH0OXIPTs', '1xgRnhW4C7o', 'mRJ8Ulll4rQ', 'dT8dmvAzIqA', 'fGqdIPer-ms', 'FQVYaX2rBAo', 'au2n7VVGv_c', 'BwmuvqFzfLI', 'wJGcwEv7838', '7Dqgr0wNyPo', 'sV2t3tW_JTQ', '6wtwpUwxQik', '6Prfg3vyZkA', 'mzB1VGEGcSU', 'LPTlvQ1Zet0', 'cuC778Gv6as', 'GaURBWLWI_0', 'xvZqHgFz51I', 'T2nHSkq13YE', 'r7qovpFAGrQ', '8UFIYGkROII', 'avFq9errZCk', '8fbyfDbi-MI', 'iuJDhFRDx9M', 'Kbj2Zss-5GY', 'oDlLTYC6OOQ', 'LKU_y_Vncs8', '9v_rtaye2yY', '_YzD9KW82sk', 'AbEHRrq7xwU', '0GbwYFqN1iE', 'EqHYnsVHXUA', 'wlN9kn1-EkQ', 'bx47iR1W4VU', 'dVfzYoriPgc', 'XXjjDXJhdHQ', 'N2Y2vQ-1m7M', 'oorVWW9ywG0', 'a9tUH2twPxc', 'hqDinxaPUK4', 'feq6MOg3qpA', 'OC7cNS0GINo', 's0PCMNels-s', '3I6-3CJd6fY', 'mxFstYSbBmc', 'jW8iiFMcS9k', 'l0U7SxXHkPY', 'bu7E2Y_GfVM', 'Mf6oZPPYIXI', 'QHwDDHDQjJA', 'kx7P_ENnDPE', 'ecopKVhf5io', 'iDGmMNUiqeI', 'A1l2qUIDFo4', 'haLIE3_3EYU', 'gRnZraoZJ8c', '-CVn3-3g_BI', 'UIt0lsBLdlw', 'nMDOSLEVdBw', 'h3EJICKwITw', 'WChdrGtdLUI', 'XEbDrIf7k9Y', 'RBXI87kpjg4', 'B5b9-Yelo0U', 'JFm7YDVlqnI', 'Yx16zJooQls', 'PbrLG5ZEV8s', 'TZrT0kdkGcc', 'BRmjopnCtTE', '2xWkATdMQms', 'EZkNUmVXg6U', 'zf99kdFw9b8', 'lbeUyW6axeA', 'wq9ATnYyJ-s', 'WJyGTRt4CQY', 'uKOf1FQZNEQ', 'mgmGXfPEUAw',
#              '4IXOM4Q2Apc', 'UCoe5x8msS4', 'RjTsQINzwl8', 'XYBCKFS-mCk', '28hYUZMufDg', 'kGV5V_VIVc8', '8_oOES_uKPI', 'K44j-sb1SRY', 'h0gxofdZ4Cw', 'qN6aWdAR1k8', '9Lw7v8dtz4E', 'W7VK4DUHvKU', 'J_-rFIxROig', '3WnLTACoSfw', 'INsVZ3ACwas', 'nceqQyqIa5o', 'k3-fAXbCa44', 'AsTnj-kLfJw', 'hzt31eJTGxo', 'Lbt3wOhMRpg', 'x8FZXaBXJK0', 'WrsFXgQk5UI', 'Bt-brUAx3Uo', 'WxL2au41cnk', '6CLNAUogWDU', 'zqflC-as2Qo', 'ca0h9TnbTIo', 'X9x7JKGa27I', 'juoznBaQbJE', 'OQ6R4TU5Vwo', 'YNyFAro1E5M', 'CnN8wb25f_8', 'w2IhccXakkE', 'Cel1TAel-eY', '_3LuZx06QhQ', 'cgMgoUmHqiw', 'PEEoaKwwxbg', 'yT7nP2gUEBI', 'MEg-oqI9qmw', 'ieTnO1Dvt-I', '7PBYGu4Az8s', 'RE68X9u_OVs', 'AqaQsL-8I_M', 'tpA5N9SvphE', 'aITIKxjFaL0', '1dvTJJvEFL8', 'Ri7W2a7r1ac', 'MibECPS132c', '2i09nOelohI', 'lqrVRKlVLXM', 'i941ldQL2L0', '63FjrdZZfp4', '3CxtK7-XtE0', '-2UprnLjkW0', 'h9CSvdiOY3M', 'F7tTxeSe_pQ', '0oBeEnY2CAQ', '6hJ4AoQE_ic', 'KpkHydjPgZg', '48O9FdteETY', 'Ta4VBDPWbSc', 'Js4haeaQBvc', 'R4Y7JIQlv20', 'ELNUK2W0aVs', 'Lm_0E9nzxKY', 'rdruKmja_mE', 'fazMSCZg-mw', '1uyYJ_QG1pc', 'VpdUaJY96-0', 'LPnnX7hOcQM', 'lkupT3nFGDE', 'o7jsf2PeYB8', 'gFA96D7Zrrw', 'q-dsUPoDr7o', 'CzhqHPuuuQo', '-G3mOwOAwT8', 'yiABohCHXUQ', 'gnC9Y8_Qpe4', '-G3mOwOAwT8', '5V6kqd-jWKg', '2BNcFDmQ7YM', 'LjkDor2LenI', '2FsnVCLYcrM', 'ZZ6VhTBcc-c', 'Jtyc--u6fUg', 'jQNazsWnQKU', 'mZu6wbj-juQ', 'cr82wSBZeeQ']

# playlist_id = create_playlist('Rap', True,
#                               settings['Authorization'], settings['Cookie'], settings['Key'])

# Add the YouTube videos to a playlist
print('[INFO] Adding videos to your YouTube playlist...')
status_code = add_videos_to_playlist(
    settings['YouTube_playlist_id'],
    # playlist_id,
    video_ids,
    settings['Authorization'],
    settings['Cookie'],
    settings['Key']
)

if status_code == 200:
    print('[INFO] Spotify playlist successfully converted to a YouTube playlist')
else:
    print('[INFO] Something went wrong, follow the steps in the README.md file')
