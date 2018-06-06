from flask import Flask, url_for, render_template
from flask import send_file, request
import glob
import json

app = Flask(__name__)


@app.route("/sounds")
def sounds():
    music = request.args["music"]
    return send_file(music, mimetype="audio/mp3")


@app.route("/")
def home():
    musiclist = glob.glob("static/musics/*.mp3")

    musicJ = [{'fileName': mi.split("/")[-1],
               "fileURL": url_for('sounds', music=mi)}
              for mi in musiclist]

    return render_template("home.html",
                           musicJ=musicJ,
                           musicJson=json.dumps(musicJ))


if(__name__ == "__main__"):
    app.run()