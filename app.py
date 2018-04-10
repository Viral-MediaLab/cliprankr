from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html', test=1)

# TODO return a json of match particpants

# TODO record results of a match 

# TODO return the top results for an emotion


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
