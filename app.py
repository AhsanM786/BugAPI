import flask
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from servicebus import p_queue

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/detect", methods=['POST'])
def detect():
    return 'OK


if __name__ == '__main__':
   app.run()
