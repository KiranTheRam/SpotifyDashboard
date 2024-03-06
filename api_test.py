import main

sp = main.auth_gen()

new_releases = main.get_new_releases(sp)
top_tracks = main.get_top_tracks(sp)
top_genres = main.get_top_genres(sp)
top_artists = main.get_top_artists(sp)
release_radar_tracks = main.get_release_radar_tracks(sp)


print("New Releases:")
for release in new_releases:
    print(release)
    # print(f"{release['name']} by {release['artist']} - {release['release_date']} - {release['url']}")

print("\nTop Tracks of the Week:")
for track in top_tracks:
    print(f"{track['name']} by {track['artist']} - {track['album']} - {track['url']}")

print("\nTop Genres of the Week:")
for genre in top_genres:
    print(genre)

print("\nTop Artists of the Week:")
for artist in top_artists:
    print(f"{artist['name']} - {artist['url']} - Image URL: {artist['image_url']}")

print("\nRelease Radar Tracks:")
for track in release_radar_tracks:
    print(f"{track['name']} by {track['artist']} - {track['release_date']} - {track['url']} - Album Art: {track['image_url']}")
