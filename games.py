"""
This module is for generating fake game data for use with the API.

An example of some game data::

    {
        "id": 1,
        "logURL": "http://derp.nope/",
        "winner": 0,
        "updates": [
            {
                "status": "complete",
                "time": "today"
            }
        ],
        "players": [
            {
                "id": 0
            },
            {
                "id": 5
            },
        ]
    }

"""
import datetime
import random

def game_data(players, count):
    now = datetime.datetime.now()
    available_players = players.items()
    player = available_players[0]

    games = {}
    for game_id in xrange(1, count+1):
        playing = (player, random.choice(available_players[1:]))
        games[game_id] = {
            "id": game_id,
            "logURL": "http://about:blank",
            "winner": random.choice(playing)[1],
            "updates": [
                {
                    "status": "complete",
                    "time": (now + datetime.timedelta(minutes=game_id)).isoformat()
                }
            ],
            "players": [{"id": player_id} for (_name, player_id) in playing]
        }

    return games
