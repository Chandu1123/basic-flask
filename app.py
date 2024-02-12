## basic flask app here...


from flask import Flask

app = Flask(__name__)

@app.route('/members')
def welcome():
    return "welcome chandu hi raa"

@app.route('/')
def welcome1():
    return "dfghjkiuytf dfghjuytrdxcvbjuytrdxcvbniuytrdxbkuytrdxcvbjuytrdxcvbjuytrxd"




if __name__ == "__main__":
    app.run(debug=True)


