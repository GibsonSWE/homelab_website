from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return "This will be a homelab dashboard"

@app.route("/resources")
def resources():
    return "This page will have some of my github resources" 

@app.route("/cml")
def cml():
    return "This page will have some information about my CML-server"

if __name__ == "__main__":
    app.run(debug=True)
