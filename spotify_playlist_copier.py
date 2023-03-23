from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def move_from_playlist_to_playlist(sp: Spotify, from_playlist_id: str, to_playlist_id: str):
    playlist = sp.user_playlist_tracks('Spotify', from_playlist_id)['items']
    song_ids = [song['track']['id'] for song in playlist]
    sp.playlist_add_items(to_playlist_id, song_ids)

if __name__ == '__main__':
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'
    sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                        client_secret=client_secret,
                                        redirect_uri=redirect_uri,
                                        scope='playlist-modify-public playlist-read-private playlist-modify-private'))
    # id of the playlist from which you want to copy all songs
    from_playlist_id = 'YOUR_PLAYLIST_ID'
    # id of the playlist to which you want to copy all songs
    to_playlist_id = 'YOUR_PLAYLIST_ID'
    move_from_playlist_to_playlist(sp, from_playlist_id, to_playlist_id)


