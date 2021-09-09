# About
This program converts a Spotify playlist into a YouTube playlist.
Note: the program only works if the selected playlist is public (so you can reach it without logging in)

# Authorization
Get Spotify API token from https://developer.spotify.com/console/get-playlist/ by clicking "GET TOKEN" and then choosing playlist-read-private and logging in. Add this token to the `config.json` file as follows:
```json
{
    "spotify": {
        "token": "{YOUR_TOKEN}"
    }
}
```