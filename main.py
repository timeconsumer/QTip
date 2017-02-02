import spotipy
import requests
import json

import sys
import spotipy
import spotipy.util as util

scopes = ['user-library-read',
          'playlist-modify-public',
          'playlist-modify-private',
          'playlist-read-collaborative',
          'playlist-read-private']

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, str.join(' ', scopes))


def create_target_playlist():
    playlists = sp.user_playlists(username)
    playlist_name = 'QTip'
    target_playlist = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            target_playlist = playlist
            print("Found playlist")
    if target_playlist is None:
        print("Couldn't find playlist, creating...")
        resp = sp.user_playlist_create(username, playlist_name, public=False)
        print(resp)
    song = find_song("ruff ryders")
    sp.user_playlist_add_tracks(username, target_playlist["id"], [song['id']])

def find_song(search_string):
    song_resp = sp.search(search_string, market="US")
    print(song_resp)
    return song_resp["tracks"]["items"][0]


if token:
    sp = spotipy.Spotify(auth=token)
    create_target_playlist()
else:
    print("Can't get token for", username)
