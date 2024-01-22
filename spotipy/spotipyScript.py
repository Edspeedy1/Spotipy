import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="",
                                                           client_secret=""))

def getTracks(uri):
    results = sp.user_playlist_tracks(playlist_id=uri)
    tracks = results['items']

    # Loops to ensure I get every track of the playlist
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


results = sp.playlist('https://open.spotify.com/playlist/4CebEyj9jOmD4RnERpVU9q?si=f1be3d8e57e0476d')
trackList = getTracks(str(results['id']))
file = open('songList.txt','w')
for idx, track in enumerate(trackList):
    file.write(track['track']['name'] + ' - ' + track['track']['artists'][0]['name'] + '\n')
file.close()