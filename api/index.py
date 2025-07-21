from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "stepr.app"

@app.route("/", methods=["GET"])
def landing():
    return render_template("index.html")

@app.route("/privacy-policy", methods=["GET"])
def privacypolicy():
    return render_template("privacypolicy.html")

@app.route("/download", method=["GET"])
def download():
    return redirect("https://apps.apple.com/us/app/stepr-walk-more-pedometer/id6748864383")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000)
