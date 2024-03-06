import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access your variables securely
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

def auth_gen():
    scope = "user-top-read user-follow-read playlist-read-private"
    # scope = "user-top-read user-follow-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=scope))
    return sp


# Dashboard Functions
def get_new_releases(sp, country='US', limit=10):
    results = sp.new_releases(country=country, limit=limit)
    albums = results['albums']['items']
    new_releases = [{
        'name': album['name'],
        'artist': album['artists'][0]['name'],
        'release_date': album['release_date'],
        'url': album['external_urls']['spotify'],
        'image_url': album['images'][0]['url'] if album['images'] else None  # Include album art URL
    } for album in albums]
    return new_releases


def get_top_tracks(sp, time_range='short_term', limit=10):
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    top_tracks = [{'name': track['name'], 'artist': track['artists'][0]['name'], 'album': track['album']['name'],
                   'url': track['external_urls']['spotify'],
                   'image_url': track['album']['images'][0]['url'] if track['album']['images'] else None} for track in
                  results['items']]
    return top_tracks


def get_top_artists(sp, time_range='short_term', limit=10):
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    top_artists = [{'name': artist['name'], 'url': artist['external_urls']['spotify'],
                    'image_url': artist['images'][0]['url'] if artist['images'] else None} for artist in
                   results['items']]
    return top_artists


def get_top_genres(sp, time_range='short_term', limit=10):
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    genres = {}
    for artist in results['items']:
        for genre in artist['genres']:
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    # Sort genres by occurrence
    sorted_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
    return [genre[0] for genre in sorted_genres][:5]  # Top 5 genres


def get_release_radar_tracks(sp, limit=10):
    # Get the current user's playlists
    playlists = sp.current_user_playlists(limit=50)

    # Find Release Radar playlist
    release_radar_id = None
    for playlist in playlists['items']:
        print(playlist['name'])
        if playlist['name'] == "Release Radar":
            release_radar_id = playlist['id']
            break

    if not release_radar_id:
        print("ERROR: mRelease Radar playlist not found.")
        return []

    # Fetch tracks from the Release Radar playlist
    results = sp.playlist_items(release_radar_id, limit=limit)
    release_radar_tracks = [{
        'name': item['track']['name'],
        'artist': item['track']['artists'][0]['name'],
        'release_date': item['track']['album']['release_date'],
        'url': item['track']['external_urls']['spotify'],
        'image_url': item['track']['album']['images'][0]['url'] if item['track']['album']['images'] else None
    } for item in results['items']]

    return release_radar_tracks
