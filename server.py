from flask import Flask
from flask import render_template
from flask import request

import argparse
import games
import json


GAMES_COUNT = 100


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('games_list.html')


@app.route("/api/")
def games_api():
    limit = request.args.get('limit') or GAMES_COUNT
    skip = request.args.get('skip') or 0
    return json.dumps(game_list[int(skip):int(skip)+int(limit)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("players",
                        type=file,
                        help="JSON file with a list of players")
    args = parser.parse_args()

    with args.players as players_file:
        players = json.load(players_file)
        game_gen = games.game_data(players, GAMES_COUNT)
        game_list = list(game_gen)

    app.run(debug=True)
