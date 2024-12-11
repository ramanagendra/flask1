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

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


## Assignemnt Try for loop

if __name__=='__main__':
    app.run(debug=True) 