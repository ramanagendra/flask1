# creating flask application 

from flask import Flask, render_template

## create the flask app
app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello World</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to flask tutorials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "<h1>the person is passed and the score is<h1> "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "<h1>the person is failed and score is<h1> "+str(score)

if __name__=='__main__':
    app.run(debug=True) 