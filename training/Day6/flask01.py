
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Hello World </h2>"

@app.route("/<uname>")
def user(uname):
    return f"<h2> Hello {uname} </h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()
