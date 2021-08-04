
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html", adject="Mera Bharath Mahan", i=150)


if __name__ == '__main__':
    app.run(debug=True)