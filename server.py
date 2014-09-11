from flask import Flask

app = Flask(__name__)


@app.route("/")
def games_list():
    return "Games be here"


@app.route("/api/")
def games_api():
    return "API be here"


if __name__ == "__main__":
    app.run()
