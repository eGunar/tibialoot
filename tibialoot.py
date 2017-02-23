from flask import Flask, render_template, request	

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
		serverlog = request.form['loot'].split("\n")
		import lootcounter
		information = lootcounter.run(serverlog)
		total_loot = 0
		for items in information:
			total_loot += items
		return render_template("counted_loot.html", alesar=information[0], rashid=information[1], nahbob=information[2], tesha=information[3], haroun=information[4], yaman=information[5], yasir=information[6], lailene=information[7], telas=information[8], tamoril=information[9], alexander=information[10], esrik=information[11], bone_master=information[12], player_items=information[13], gold=information[14], total=total_loot)
	else:	
		return render_template("lootcounter.html")

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)