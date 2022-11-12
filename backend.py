import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import random # omegalul
import extra

# useful resources:
# https://spotipy.readthedocs.io/en/2.21.0/
# https://jsonviewer.com
# https://developer.spotify.com/documentation/web-api/

# TODO:
# - add album / saved songs support
# - GUI
# - other forms of shuffling
# - deshittify codebase

scope = ("user-library-read", "playlist-read-private", "playlist-read-collaborative", "user-modify-playback-state", "user-read-currently-playing")
settings = dotenv.dotenv_values(".env")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=settings['CLIENT_ID'],client_secret=settings['CLIENT_SECRET'],redirect_uri=settings['REDIRECT_URI']))

playlists = sp.current_user_playlists()['items']

picked = extra.pick_playlist(sp,playlists)
# picked = playlists[3]

results = sp.playlist_tracks(picked['id'])
tracks:list = results['items']
while results['limit'] + results['offset'] < results['total']:
	results = sp.playlist_tracks(picked['id'],offset=len(tracks))
	tracks.extend(results['items'])

new_queue = list[str]()
for i in range(90):
	track = random.choice(tracks)['track']
	print(i,track['artists'][0]['name']," - ",track['name'])
	new_queue.append(track['id'])
print(new_queue)

for track in new_queue:
	sp.add_to_queue(track)