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




@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
   app.run()
