# Building URL dynamically
    
## this is variable rules


from flask import Flask,redirect,url_for 

app = Flask(__name__)


@app.route('/')
def welcome():
    return "WELCOMEEEEEE................................"

@app.route('/succ/<int:score>')
def chandu(score):
    return "the score is "+str(score)+"he passeddddddddddddddddddddddddddddd"

@app.route('/fail/<int:score>')
def chandu1(score):
    return "the person scored less ...so failed and the score  is "+str(score)+"failed..........😒"


@app.route('/results/<int:marks>')
def chandu2(marks):
    result =""
    if marks  < 50:
        result= "chandu1"
    else:
        result= "chandu"
    return redirect(url_for(result, score=marks))




if __name__=="__main__":
    app.run(debug=True)