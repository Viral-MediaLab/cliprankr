from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html', test=1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
