
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index3.html", uname=name, content="One stop for all type of fruits...",
                    fruits=['Apple', 'Orange', 'Pine', 'Grapes', 'Banana', 'Watermelon'])

if __name__ == '__main__':
    app.run(debug=True)
