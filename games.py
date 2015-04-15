"""
This module is for generating fake game data for use with the API.

An example of some game data::

    {
        "id": 1,
        "logURL": "http://derp.nope/",
        "updates": [
            {
                "status": "complete",
                "time": "today"
            }
        ],
        "players": [
            {
                "name": "Team Awesome",
                "score": 1
            },
            {
                "name": "Team Less Awesome",
                "score": 0
            },
        ]
    }

"""
import datetime
import random

def game_data(players, count):
    now = datetime.datetime.now()
    player = players[0]
    for id in xrange(1, count+1):
        players = (player, random.choice(players[1:]))

        scores = [0, 1]
        random.shuffle(scores)

        yield {
            "id": id,
            "logURL": "about:blank",
            "updates": [
                {
                    "status": "complete",
                    "time": str(now + datetime.timedelta(minutes=id))
                }
            ],
            "players": dict(zip(players, scores)),
        }
