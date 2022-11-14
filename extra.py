import spotipy

def pick_playlist(sp:spotipy.Spotify,playlists:list[dict]) -> dict:
	print("Pick a playlist to shuffle through:")
	for i,list in enumerate(playlists):
		print(f"{i} - {list['name']}")
	selection = input("> ")
	try:
		return playlists[int(selection)]
	except ValueError:
		return sp.playlist(selection)
	except IndexError:
		print(f"Value not between 0 and {len(playlists) - 1}; please try again or use ^C to quit.")
		return pick_playlist(playlists)

SCOPES = ("user-library-read", "playlist-read-private", "playlist-read-collaborative", "user-modify-playback-state", "user-read-currently-playing")