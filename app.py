from flask import Flask

app = Flask(__name__)

@app.route('/potato')
def welcome():
    return "Hello World!"

@app.route('/')
def rootpage():
    return "Second page"

@app.route('/bob')
def bobpage():
    return "Yo bob"
    

app.run()