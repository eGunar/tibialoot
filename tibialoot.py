from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_security import Security, PeeweeUserDatastore, login_required
from models import *
from forms import *
import os

app = Flask("tibialoot")
app.config["WTF_CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")

app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = "email"
app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
app.config["SECURITY_PASSWORD_SALT"] = app.config["SECRET_KEY"]
app.config['SECURITY_REGISTERABLE'] = True
app.config["SECURITY_SEND_REGISTER_EMAIL"] = False

user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

@app.route("/set_session")
def track_session():
	is_logged_in = int(session.get("is_logged_in", 0))
	if is_logged_in:
		print("hej")
	else:
		print("Nej")

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/spawn_statistics/")
def spawn_statistics():
	return render_template("spawn_statistics.html")

@app.route("/boss_statistics/")
def boss_statistics():
    return render_template("boss_statistics.html")

@app.route("/online_check/")
@login_required
def onlinecheck():
	return render_template("online_check.html")

@app.route("/lootcounter/", methods=["GET", "POST"])
@login_required
def lootcounter():
	if request.method == "POST":
		npc_list = [Alesar, Rashid, Nahbob, Tesha, Haroun, Yaman, Yasir, Lailene, Telas, Tamoril, Alexander, Esrik, Bone_master, Player_items, Gold]
		huntname = request.form['huntinglocation']
		serverlog = request.form['loot'].split("\n")
		import lootcounter
		information = lootcounter.run(serverlog)
		total_loot = 0
		for items in information:
			total_loot += items[1]
		return render_template("counted_loot.html", information=information, total=total_loot, huntname=huntname, npc_list=npc_list)
	else:
		npc_list = [Alesar, Rashid, Nahbob, Tesha, Haroun, Yaman, Yasir, Lailene, Telas, Tamoril, Alexander, Esrik, Bone_master, Player_items, Gold]
		return render_template("lootcounter.html", npc_list=npc_list)

@app.route("/about/", methods=["GET", "POST"])
def about():
	contact_form = ContactForm()
	if contact_form.validate_on_submit():
		return "Hejjsan"
	else:
		return render_template("about.html", contact_form=contact_form)


if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)