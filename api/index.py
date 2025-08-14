from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "stepr.app"

@app.route("/", methods=["GET"])
def landing():
    return render_template("index.html")

@app.route("/download", methods=["GET"])
def download():
    return redirect("https://apps.apple.com/us/app/glupi/id6749968777")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000, debug = True)
