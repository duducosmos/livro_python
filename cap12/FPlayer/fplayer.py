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
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
	MAIL_USE_SSL=False,
	MAIL_USERNAME = "meuemail@gmail.com",
	MAIL_PASSWORD = "minhasenha"
	)

mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = model()
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['pw']
        query = db(db.user.email == email)
        if query.isempty() is True:
            password = sha256_crypt.encrypt(password)
            db.user.insert(name=name,
                           email=email,
                           password=password)
            db.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html')

    else:
        return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	if flask_login.current_user.is_authenticated:
		return redirect(url_for("home"))

	if request.method == 'GET':
		return render_template("login.html")

	email = request.form['email']
	password = request.form['pw']

	user = User(email, password)

	if user.get_id() is None:
		return render_template("login.html")

	flask_login.login_user(user)
	return redirect(url_for('home'))


@app.route("/sounds")
def sounds():
    music = request.args["music"]
    return send_file(music, mimetype="audio/mp3")


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
@flask_login.login_required
def home():
    updatemusic()
    musicJ = get_musics()
    return render_template("home.html",
                           musicJ=musicJ,
                           username=flask_login.current_user.name)

if(__name__ == "__main__"):
    app.run(debug=True)