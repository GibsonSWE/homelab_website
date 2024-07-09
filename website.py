from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/resources")
def resources():
    return render_template("resources.html") 

@app.route("/cml")
def cml():
    return render_template("cml.html")

if __name__ == "__main__":
    app.run(debug=True)
