from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('games_list.html')


@app.route("/api/")
def games_api():
    return "API be here"


if __name__ == "__main__":
    app.run(debug=True)
