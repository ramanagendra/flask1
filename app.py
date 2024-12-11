# creating flask application 

from flask import Flask

## create the flask app
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/')
def home():
    return "Hello World"

if __name__=='__main__':
    app.run(debug=True) 