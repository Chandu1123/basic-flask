### learning here integrate html with flask 

###Http work like get and post


from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/succ/<int:score>')
def succ(score):
    res  = " "
    if score >=50:
        res = "SUCCESS"
        
    else:
        res = "FAIL"

    return render_template('result.html', result=res)
    
    

    
@app.route('/fail/<int:score>')
def fail(score):
    return "the person scored less ...so failed and the score  is "+str(score)+"failed..........😒"


@app.route('/results/<int:marks>')
def results(marks):
    result =" "
    if marks  < 50:
        result= "fail"
    else:
        result= "succ"
    return redirect(url_for(result, score=marks))



@app.route('/submit', methods=['POST','GET'])
def submit():
    total_marks = 0 
    if request.method == 'POST':
        maths = float(request.form['maths'])
        AIML = float(request.form['AIML'])
        Computervision = float(request.form['Computer-vision'])
        Deeplearning = float(request.form['Deep-learning'])
        total_marks = (maths + AIML + Deeplearning + Computervision)/4
    
    res = " "
    if total_marks > 50 :
        res= "succ"
    else:
        res = "fail"
    
    return redirect(url_for(res,score=total_marks))


if __name__=="__main__":
    app.run(debug=True)
