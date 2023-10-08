from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="color:green">Welcome to Java Home  </h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=80)
