from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
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

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")


# HOMELAB DROPDOWN
@app.route("/homelab/overview")
def homelab_overview():
    return render_template("/homelab/overview.html")

@app.route("/homelab/components")
def homelab_components():
    return render_template("/homelab/components.html")

@app.route("/homelab/network")
def homelab_network():
    return render_template("/homelab/network.html")

@app.route("/homelab/future_plans")
def homelab_future_plans():
    return render_template("/homelab/future_plans.html")



if __name__ == "__main__":
    app.run(debug=True)
