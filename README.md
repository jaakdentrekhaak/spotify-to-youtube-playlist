# About
This program converts a Spotify playlist into a YouTube playlist.
Note: this program is meant for personal use, but you can also use it if you have a Spotify client_id and client_secret see https://developer.spotify.com/documentation/general/guides/authorization-guide/).

# Spotify
To interact with the Spotify API, you need a client_id and client_secret. This can be found on the Spotify developers dashboard after creating an application: https://developer.spotify.com/dashboard/applications. The client_id and client_secret need to be added to the `config.json` file in the root folder like this, where you have to replace the values:
```json
{
    "spotify": {
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET"
    }
}
```
More information about the authorization can be found [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/).

The only thing the Spotify part needs, apart from the client_id and client_secret, is the ID of the playlist you want to convert to YouTube. You can find the playlist ID by going to the playlist in the browser or desktop application, clicking the button with tree dots and choosing 'share > copy playlist link'. The only part that matters from the copied URL is the playlist ID. If the URL of the playlist is 'https://open.spotify.com/playlist/1obKlPpsy6x2Ad9cFem4jF', then the playlist ID is '1obKlPpsy6x2Ad9cFem4jF'. Add this playlist ID to the field 'Spotify_playlist_id' in the file `settings.json` in the root folder of this project.

# YouTube
## Getting video ids
If we got the names of the songs and artists from the Spotify API, we have to search the corresponding video on YouTube. This part happens automatically by this program.

## Adding video to playlist
Once the video ids for all the songs are retrieved, we have to add these songs to our playlist. You can choose to automatically create a new playlist or add songs to an existing playlist. To add the videos to an existing playlist, add the playlist ID to the 'YouTube_playlist_id' field . The playlist ID can be found by going to your playlist on YouTube and inspecting the URL. If the URL looks like 'https://www.youtube.com/playlist?list=PL633QL57LZ0W7wiYJE3p7z6OvpYmiUu7r', then the ID is 'PL633QL57LZ0W7wiYJE3p7z6OvpYmiUu7r'. To let the program create a new playlist, the value of the field 'YouTube_playlist_id' in the file `settings.json` doesn't matter.

### Authentication
Adding songs to a playlist requires you to be logged in to your account. That's why you first need to login to YouTube on your normal browser. The following strategy comes from [ytmusicapi](https://github.com/sigma67/ytmusicapi).

To run authenticated requests you need to set up you need to copy your request headers from a POST request in your browser. To do so, follow these steps:
- Open a new tab
- Open the developer tools (Ctrl-Shift-I or F12) and select the “Network” tab
- Go to https://www.youtube.com and ensure you are logged in
- Find an authenticated POST request. The simplest way is to filter by '/browse' using the search bar 'Filter URLs' of the developer tools and select the POST request (if you don't see the request, just select one of the POST requests) and go to the 'Headers' tab.

In the 'Headers' tab, first copy the authentication key which can be found inside the URL where the POST request is made to and add it to the field 'Key' in the file `settings.json` in the root folder of this project. Head back to the browser and in the 'Headers' tab, scroll down to the 'Request Headers', enable 'Raw' view (important) and copy the values for the 'Authorization' and 'Cookie' fields and also add them to the `settings.json` file to the fields "Authorization" and "Cookie" respectively.

The `settings.json` file in the root folder looks like this, where you have to replace the values:
```json
{
    "Spotify_playlist_id": "YOUR_SPOTIFY_PLAYLIST_ID",
    "YouTube_playlist_id": "YOUR_YOUTUBE_PLAYLIST_ID",
    "Authorization": "YOUR_AUTHORIZATION",
    "Cookie": "YOUR_COOKIE",
    "Key": "YOUR_KEY"
}
```

## YouTube API (not used)
To interact with the YouTube API (function `youtube.py`), you also need a YouTube API key, which also has to be added to the `config.json` file.

Add this to the `config.json` file, where you have to replace the value:
```json
{
    "youtube": {
        "api_key": "YOUR_YOUTUBE_API_KEY"
    }
}
```

# Development
NOTE: the files config.json and settings.json are ignored by git after pushing the first 'default' version, see [here](https://stackoverflow.com/questions/18276951/how-do-i-stop-git-from-tracking-any-changes-to-a-file-from-this-commit-forward)