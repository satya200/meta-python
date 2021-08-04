
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template("index04.html", uname=name)

if __name__ == '__main__':
    app.run(debug=True)
