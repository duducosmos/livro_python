from flask import Flask, url_for, render_template
from flask import send_file, request, flash, redirect

import flask_login
from passlib.hash import sha256_crypt
from flask_mail import Mail

import datetime

from tools import *
from model import model
from user import User


app = Flask(__name__)
app.secret_key = "iojsapklamnsetoiaqwerb"

login_manager = flask_login.LoginManager()

login_manager.init_app(app)


app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp-relay.sendinblue.com',
    MAIL_PORT=587,
    MAIL_USE_SSL=False,
    MAIL_USERNAME="pereira.somoza@gmail.com",
    MAIL_PASSWORD="w4ZsMVPQh6rq2KtW"
)

mail = Mail(app)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@app.route("/sounds")
def sounds():
    music = request.args["music"]
    return send_file(music, mimetype="audio/mp3")


@app.route("/alternativCoverImage")
def alternativCoverImage():
    return app.send_static_file('images/noCoverImage.png')


@app.route("/coverImage")
def coverImage():
    cover = request.args["music"]
    cover = File(cover)
    if("APIC:" in cover.tags.keys()):
        imgcover = cover.tags["APIC:"].data
        strIO = BytesIO()
        strIO.write(imgcover)
        strIO.seek(0)

        return send_file(strIO,
                         mimetype="image/jpg")
    else:
        return app.send_static_file('images/noCoverImage.png')


@app.route("/")
def home():


    updatemusic()
    musicJ = get_musics()


    return render_template("home.html",
                           musicJ=musicJ,
                           username="Fplayer")


if(__name__ == "__main__"):
    app.run(debug=True)
