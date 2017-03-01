from flask import Flask, render_template, request
from models import *	

app = Flask("tibialoot")

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
		print(npc_list)
		return render_template("counted_loot.html", information=information, total=total_loot, huntname=huntname, npc_list=npc_list)
	else:
		npc_list = [Alesar, Rashid, Nahbob, Tesha, Haroun, Yaman, Yasir, Lailene, Telas, Tamoril, Alexander, Esrik, Bone_master, Player_items, Gold]
		return render_template("lootcounter.html", npc_list=npc_list)

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)