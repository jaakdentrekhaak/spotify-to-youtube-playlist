# About
This program converts a Spotify playlist into a YouTube playlist.
Note: this program is not meant to be used by other people than me, since you need to have a client_id and client_secret (unless you have your own client_id and client_secret)

# Development
The client_id and client_secret for Spotify for this project can be found on my Spotify developers dashboard: https://developer.spotify.com/dashboard/applications. The client_id and client_secret need to be added to a `config.json` file in the root folder.

To interact with the YouTube API, you also need a YouTube API key, which also has to be added to the `config.json` file.

The `config.json` file will look like this:
```json
{
    "spotify": {
        "client_id": "",
        "client_secret": ""
    },
    "youtube": {
        "api_key": ""
    }
}
```