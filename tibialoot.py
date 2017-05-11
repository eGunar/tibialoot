from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_security import Security, PeeweeUserDatastore, login_required	
from models import *
from forms import *
import os

app = Flask("tibialoot")
app.config["WTF_CSRF_ENABLED"] = False 
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")


app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = "email"
app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
app.config["SECURITY_PASSWORD_SALT"] = app.config["SECRET_KEY"]

user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)


"""
@app.route("/recipie/")
def track_cookie():
	visits = int(request.cookies.get("number_of_visits", 0))
	visited = False
	if visits >= 1:
		visited = True
	visits += 1
	resp = make_response(render_template("recipie.html", visited=visited, visits=visits))
	resp.set_cookie("number_of_visits", str(visits), 60*60*24*7)
	return resp"""

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


"""
@app.route("/login/", methods=["GET", "POST"])
def log_in():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		if login_form.password.data == "häst":
			print(login_form.password.data)
			session["loggedin"] = True
			return redirect(url_for("recipie"))
		else:
			return render_template("recipie.html", login_form=login_form)
	else:	
		return render_template("recipie.html", login_form=login_form)

@app.route("/recipie")
def recipie():
	logged_in = session.get("loggedin", 0)
	if logged_in:
		return "HEJASNA"
	else:
		return "Access Denied"
"""
if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)