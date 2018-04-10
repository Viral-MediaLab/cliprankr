from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html', test=1)

# TODO query for two short videos, save their urls and videos to a new location

# TODO return a json of match particpants

# TODO record results of a match
# curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:5000/record

@app.route('/record', methods=['POST'])
def recordresults():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)

# TODO return the top results for an emotion


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
