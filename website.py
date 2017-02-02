from flask import Flask, render_template

app = Flask("tibialoot")

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/loot_statistics/")
def loot_statistics():
	return render_template("loot_statistics.html")

@app.route("/boss_statistics/")
def boss_statistics():
    return render_template("boss_statistics.html")

@app.route("/online_check/")
def onlinecheck():
	return render_template("online_check.html")

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)