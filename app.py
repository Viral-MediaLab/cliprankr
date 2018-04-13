import json
from random import randint
from flask import Flask, render_template, request, redirect
from trueskill import Rating, quality_1vs1, rate_1vs1

app = Flask(__name__)

@app.route('/')
def homepage():

    # TODO query for two short videos, save their urls and videos to a new location (or do this in SG)?
    # how do we pick a match, make sure 1 of the videos is new (if there are unranked videos).

    # select an emotion for battle, then retrieve current ratings from the two videos
    # alice, bob = Rating(250), Rating(500)

    # TODO if either video does not have a rating for this emotion apply a default rating of 500

    # TODO return a json of match particpants and videos
    #if quality_1vs1(alice, bob) < 0.50:
        # this may be interesting for analytics...?
        # print('This match seems to be not so fair')

    # for x in range(0, 10):
    #     if randint(0, 9)%2 == 0:
    #         alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
    #     else:
    #         bob, alice = rate_1vs1(bob, alice)
    #
    # print(alice)
    # print(bob)
    # for x in range(0, 1000):
    #     if randint(0, 9)%2 == 0:
    #         alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
    #     else:
    #         bob, alice = rate_1vs1(bob, alice)
    # print(alice)
    # print(bob)

    return render_template('home.html', test=1)

# TODO record results of a match, NOW just receives json
# curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:5000/record
@app.route('/record', methods=['POST'])
def recordresults():
    if not request.json:
        abort(400)
    print("ok :)")
    print(request.json)

    # create two ratings objects from the db data
    #alice, bob = Rating(250), Rating(500)

    # who won?
    #if randint(0, 9)%2 == 0:
    #    alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
    #else:
    #    bob, alice = rate_1vs1(bob, alice)

    # update respective ratings in db

    return json.dumps(request.json)

# TODO return the top results for an emotion
@app.route('/results/<emotion>', methods=['GET'])
def retrieveresults():
    return render_template('results.html', emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
