import flask
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory


CONNECTION_STR = "Endpoint=sb://jcbugsystem.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RnKgBHavWXnydS3wUygMQaBT/b7/bXDTWFEjtd5P2zY="
PRIO_QUEUE_NAME = "priorityqueue"
STANDARD_QUEUE_NAME = "standardqueue"
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

app = Flask(__name__)
app.config["DEBUG"] = True

def send_prio_message(sender):
    msg = json.dumps({
	"severity": "black",
	"triage": "asdasdasda aSF ASFG ADEG  gqweg gq1 13 41 fa n 133r ",
	"team" : "pearl",
    "title" : "test"
    })
    message = ServiceBusMessage(msg)
    sender.send_messages(message)
    print("Sent a priority message")

def send_standard_message(sender):
    message = ServiceBusMessage("Standard bug")
    sender.send_messages(message)
    print("Sent a standard message")



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
   app.run()
