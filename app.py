import flask
import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
   app.run()
