import flask
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True
CONNECTION_STR = os.environ['ENDPOINT']
PRIO_QUEUE_NAME = "priorityqueue"

@app.route('/')
def index():
    
    msg = json.dumps({
	"severity": "black",
	"triage": "asdasdasda aSF ASFG ADEG  gqweg gq1 13 41 fa n 133r ",
	"team" : "pearl",
        "title" : "test"
    })
    with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
        with client.get_queue_sender(queue_name=PRIO_QUEUE_NAME) as sender:
            message = ServiceBusMessage(msg)
            sender.send_messages(message)
    return render_template('index.html')

if __name__ == '__main__':
   app.run()
