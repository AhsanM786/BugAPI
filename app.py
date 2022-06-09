import flask
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    CONNECTION_STR = "Endpoint=sb://jcbugsystem.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RnKgBHavWXnydS3wUygMQaBT/b7/bXDTWFEjtd5P2zY="
    PRIO_QUEUE_NAME = "priorityqueue"
    STANDARD_QUEUE_NAME= "standardqueue"
    msg= json.dumps(request.json)
    postMessage = json.loads(msg)
    
    if "severity" in postMessage:
        if postMessage["severity"] == "black":
            
            with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                with client.get_queue_sender(queue_name=PRIO_QUEUE_NAME) as sender:
                    message = ServiceBusMessage(msg)
                    sender.send_messages(message)
            return 'Severe bug report'
        elif postMessage["severity"] == "red":
            with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                with client.get_queue_sender(queue_name=STANDARD_QUEUE_NAME) as sender:
                    message = ServiceBusMessage(msg)
                    sender.send_messages(message)
            return 'Standard bug report'
        elif postMessage["severity"] == "blue":
            with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
                with client.get_queue_sender(queue_name=STANDARD_QUEUE_NAME) as sender:
                    message = ServiceBusMessage(msg)
                    sender.send_messages(message)
            return 'Standard bug report'
        else:
            with open("log.txt", 'a') as json_file:
                json.dump(request.json, json_file, indent=4, separators=(',',': '))
            return 'Does not match required severity'
    else:
        with open("log.txt", 'a') as json_file:
            json.dump(request.json, json_file, indent=4, separators=(',',': '))
        return  'Missing severity' 
    return 'OK'

if __name__ == '__main__':
   app.run()
