import json
from random import randint
from flask import Flask, render_template, request, redirect, abort
from trueskill import Rating, quality_1vs1, rate_1vs1

app = Flask(__name__)

def get_vids():
    videoMatches = [
          "http://um-bubble.media.mit.edu:10022/static/1523404819916.http-um-bubble-media-mit-edu-10022-static-1523401236092-9ea6f6f6-c838-45de-8dce-72ed8ae02ba3-mp4_nocom.mp4#t=1031,1054",
          "http://um-bubble.media.mit.edu:10022/static/1523465136895.5b67ac90-d9f1-494d-9ebc-65fae5458daf.mp4#t=863,886",
          "http://um-bubble.media.mit.edu:10022/static/1523458789994.http-um-bubble-media-mit-edu-10022-static-1523451617858-58b3fb41-ceca-4cad-a29f-fc7586ca779b-mp4_nocom.mp4#t=119,142",
          "http://um-bubble.media.mit.edu:10022/static/1523460719539.0481da84-48db-4cd6-aa99-d67cac28b418.mp4#t=6,29",
          "http://um-bubble.media.mit.edu:10022/static/1523418962483.http-um-bubble-media-mit-edu-10022-static-1523417414283-4c1e3933-b142-417b-88cc-9576195f7dbc-mp4_nocom.mp4#t=206,229",
          "http://um-bubble.media.mit.edu:10022/static/1523423636388.http-um-bubble-media-mit-edu-10022-static-1523421041389-aa5d65af-876e-4042-8996-b839e995c95d-mp4_nocom.mp4#t=829,852",
          "http://um-bubble.media.mit.edu:10022/static/1523260159365.http-um-bubble-media-mit-edu-10022-static-1523255934329-7496ccec-caf7-418c-b79c-ca45bbd283ea-mp4_nocom.mp4#t=758,781",
          "http://um-bubble.media.mit.edu:10022/static/1523271422272.f3cd2708-341a-41fc-b56f-a3f8c5927fcf.mp4#t=1196,1219",
          "http://um-bubble.media.mit.edu:10022/static/1523262433366.b9b47a1a-4f45-4aff-8fd0-b2c149242a1a.mp4#t=11,34",
          "http://um-bubble.media.mit.edu:10022/static/1523211467792.9b4cdc65-5e3a-4581-96c8-a9c2d6a8404b.mp4#t=487,510",
          "http://um-bubble.media.mit.edu:10022/static/1522969033756.373b7035-8e55-443f-984b-8219ff8dd2ef.mp4#t=0,10",
          "http://um-bubble.media.mit.edu:10022/static/1523021235932.4c04a18f-491b-48a5-b7c4-97b5f71d5895.mp4#t=0,10",
          "http://um-bubble.media.mit.edu:10022/static/1522996513264.bc48a12c-0af7-4eae-aa72-06281e7a0fcb.mp4#t=377,400",
          "http://um-bubble.media.mit.edu:10022/static/1523018768188.http-um-bubble-media-mit-edu-10022-static-1523014202988-001d2629-4a77-4e81-8a44-4f83851b562f-mp4_nocom.mp4#t=1067,1090",
          "http://um-bubble.media.mit.edu:10022/static/1523412675524.http-um-bubble-media-mit-edu-10022-static-1523403041741-5c186ad9-bae9-4543-b536-63a2fc1cd2f1-mp4_nocom.mp4#t=523,546",
          "http://um-bubble.media.mit.edu:10022/static/1523412675524.http-um-bubble-media-mit-edu-10022-static-1523403041741-5c186ad9-bae9-4543-b536-63a2fc1cd2f1-mp4_nocom.mp4#t=776,799"
        ]
    rand1, rand2 = 0, 0
    while rand1 == rand2:
        rand1 = randint(0, len(videoMatches)-1)
        rand2 = randint(0, len(videoMatches)-1)

    toConsider = ["Relief", "Joy", "Excitement", "Wonder", "Dislike", "Loathing", "Nervousness", "Desperation", "Panic", "Fury", "Frustration", "Exasperation", "Disappointment", "Hopelessness", "Grief", "Agitation", "Calm"]

    obj = { 'tournament_id' : toConsider[randint(0, len(toConsider)-1)],
            'match_id' : randint(0, 100),
            'participants' : [
                {
                    '_id' : rand1,
                    'videoUrl' : videoMatches[rand1]
                },
                {
                    '_id' : rand2,
                    'videoUrl' : videoMatches[rand2]
                }
            ]
        }

    return obj

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
    #print(request.get_json(force=True))

    # create two ratings objects from the db data
    #alice, bob = Rating(250), Rating(500)

    # who won?
    #if randint(0, 9)%2 == 0:
    #    alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
    #else:
    #    bob, alice = rate_1vs1(bob, alice)

    # update respective ratings in db

    return json.dumps(get_vids()) # json.dumps(request.json)

# TODO return the top results for an emotion
@app.route('/results/<emotion>', methods=['GET'])
def retrieveresults(emotion):
    return render_template('results.html', emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
