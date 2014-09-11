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
    for id in xrange(count):
        yield {
            "id": id,
            "logURL": "about:blank",
            "updates": [
                {
                    "status": "complete",
                    "time": str(now + datetime.timedelta(minutes=id))
                }
            ],
            "players": dict(zip(random.sample(players, 2), (0, 1))),
        }
