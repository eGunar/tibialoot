from flask import Flask, render_template

app = Flask("tibialoot")

visits = 0

@app.route("/")
def home():
	global visits
	visits += 1
	name = "Erik"
	return render_template("home.html", username=name, visits=visits)

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)