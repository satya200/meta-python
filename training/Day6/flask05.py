
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<uname>")
def home(uname):
    return render_template("index2.html", uname=uname, content="Iterations using For Loop...")


if __name__ == '__main__':
    app.run(debug=True)