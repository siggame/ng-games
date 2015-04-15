from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

import argparse
import games
import json


GAMES_COUNT = 100


app = Flask(__name__)


@app.route("/competition/<competition>/games/")
def index(competition):
    return render_template('index.html')


@app.route("/api/competition/<competition>/games/<id>/")
def game_api(competition, id):
    return json.dumps(games[competition][id])


@app.route("/api/competition/<competition>/games/")
def games_api(competition):
    limit = request.args.get('limit') or GAMES_COUNT
    skip = request.args.get('skip') or 0
    game_list = games[competition].values()
    print game_list
    return json.dumps(game_list[int(skip):int(skip)+int(limit)])


@app.route("/api/competition/<competition>/teams/")
def teams_api(competition):
    return json.dumps([{"id": i, "name": n} for n, i in teams[competition].iteritems()])


@app.route("/api/competition/<competition>/team/")
def team_api(competition):
    team = my_teams[competition]
    return json.dumps({"name": team, "id": teams[competition][team]})


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("players",
                        type=file,
                        help="JSON file with a list of players")
    args = parser.parse_args()

    with args.players as players_file:
        teams = json.load(players_file)

    games = {c: games.game_data(d, GAMES_COUNT) for c, d in teams.iteritems()}
    my_teams = {c: ts.keys()[0] for c, ts in teams.iteritems()}

    app.run(debug=True)
