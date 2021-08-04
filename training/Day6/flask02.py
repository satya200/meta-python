

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome</h1> <h2> Hello World </h2>"

@app.route("/<uname>")
def user(uname):
    return f"<h2> Hello {uname} </h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("user", uname="root"))

if __name__ == '__main__':
    app.run(debug=True)
