from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/rahat/<int:number1>/<int:number2>")
def hello(number1,number2):
    divresult=number1/number2
    return "Hello Rahat %d" %divresult

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)