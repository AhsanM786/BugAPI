import flask
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['/post_json', 'POST'])
def index():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        file = request.json
    else:
        return 'Content-Type not supported!'
    CONNECTION_STR = "Endpoint=sb://jcbugsystem.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RnKgBHavWXnydS3wUygMQaBT/b7/bXDTWFEjtd5P2zY="
    PRIO_QUEUE_NAME = "priorityqueue"
    STANDARD_QUEUE_NAME= "standardqueue"

    for i in range(len(file)):
        msg = json.dumps(file[i])
        postMessage = json.loads(msg)
        if "severity" in postMessage:
            if postMessage["severity"] == "black":
                with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                    with client.get_queue_sender(queue_name=PRIO_QUEUE_NAME) as sender:
                        message = ServiceBusMessage(msg)
                        sender.send_messages(message)
            elif postMessage["severity"] == "red":
                with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                    with client.get_queue_sender(queue_name=STANDARD_QUEUE_NAME) as sender:
                        message = ServiceBusMessage(msg)
                        sender.send_messages(message)
            elif postMessage["severity"] == "blue":
                with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                    with client.get_queue_sender(queue_name=STANDARD_QUEUE_NAME) as sender:
                        message = ServiceBusMessage(msg)
                        sender.send_messages(message)
            else:
                with open("log.txt", 'a') as json_file:
                    json.dump(postMessage, json_file, indent=4, separators=(',',': '))
        else:
            with open("log.txt", 'a') as json_file:
                json.dump(postMessage, json_file, indent=4, separators=(',',': '))

    return 'OK'

if __name__ == '__main__':
   app.run()
