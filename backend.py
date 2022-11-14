import spotipy
from spotipy.oauth2 import SpotifyOAuth
from settings import Settings
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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=extra.SCOPES,client_id=Settings.client_id,client_secret=Settings.client_id,redirect_uri=Settings.client_id))

def list_playlists():
	return sp.current_user_playlists()['items']

def get_track_list(playlist:dict) -> list:
	results = sp.playlist_tracks(playlist['id'])
	tracks:list = results['items']
	while results['limit'] + results['offset'] < results['total']:
		results = sp.playlist_tracks(playlist['id'],offset=len(tracks))
		tracks.extend(results['items'])
	return tracks

def create_queue(tracks:list):
	new_queue = list[str]()
	for i in range(Settings.added_songs):
		track = random.choice(tracks)['track']
		# print(i,track['artists'][0]['name']," - ",track['name'])
		new_queue.append(track['id'])
	return new_queue

def add_to_queue(queue:list[str]):
	for track in queue:
		sp.add_to_queue(track)

def main():
	playlists = list_playlists()

	picked = extra.pick_playlist(sp,playlists)
	# picked = playlists[3]

	tracks = get_track_list(picked)
	new_queue = create_queue(tracks)
	add_to_queue(new_queue)

if __name__ == "__main__":
	pass