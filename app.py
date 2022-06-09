import flask
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    msg = json.dumps({
	"severity": "black",
	"triage": "asdasdasda aSF ASFG ADEG  gqweg gq1 13 41 fa n 133r ",
	"team" : "pearl",
        "title" : "test"
    })
    ENDPOINT=os.environ['ENDPOINT']
    with ServiceBusClient.from_connection_string(ENDPOINT) as client:
        with client.get_queue_sender(queue_name="priorityqueue") as sender:
            message = ServiceBusMessage(msg)
            sender.send_messages(message)
    return render_template('index.html')

if __name__ == '__main__':
   app.run()
