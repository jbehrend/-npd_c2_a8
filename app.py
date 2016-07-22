from flask import Flask
import datetime

app = Flask(__name__)
now = datetime.datetime.now()

@app.route('/')
def intro():
    return "Jean's first web application"

@app.route('/helloworld')
def helloworld():
    return "Hello, World!"

@app.route('/currentservertime')
def currentservertime():
    return str(now)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
