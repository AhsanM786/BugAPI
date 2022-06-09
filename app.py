import os
import json
from servicebus import p_queue
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/detect", methods=['POST'])
def detect():
    msg = json.dumps({"severity": "black","triage": "asdasdasda aSF ASFG ADEG  gqweg gq1 13 41 fa n 133r ","team" : "pearl","title" : "test"})
    p_queue(msg)
    return 'OK'

if __name__ == '__main__':
   app.run()
