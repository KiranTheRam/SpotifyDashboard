from flask import Flask, render_template
import main

app = Flask(__name__)


@app.route('/')
def dashboard():
    sp = main.auth_gen()

    new_releases = main.get_new_releases(sp)
    top_tracks = main.get_top_tracks(sp)
    top_artists = main.get_top_artists(sp)
    top_genres = main.get_top_genres(sp)
    release_radar_tracks = main.get_release_radar_tracks(sp)
    # return render_template('dashboard.html', new_releases=new_releases, top_tracks=top_tracks, top_artists=top_artists, top_genres=top_genres, release_radar_tracks=release_radar_tracks)
    return render_template('pretty_dash.html', new_releases=new_releases, top_tracks=top_tracks, top_artists=top_artists, top_genres=top_genres, release_radar_tracks=release_radar_tracks)


if __name__ == '__main__':
    app.run(debug=True)
