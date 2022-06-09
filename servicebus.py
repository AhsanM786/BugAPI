from azure.servicebus import ServiceBusClient, ServiceBusMessage

STANDARD_QUEUE_NAME = "standardqueue"

def p_queue(msg):
    CONNECTION_STR = "Endpoint=sb://jcbugsystem.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RnKgBHavWXnydS3wUygMQaBT/b7/bXDTWFEjtd5P2zY="
    PRIO_QUEUE_NAME = "priorityqueue"
    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_sender(queue_name=PRIO_QUEUE_NAME) as sender:
            message = ServiceBusMessage(msg)
            sender.send_messages(message)

def s_queue(msg):
    CONNECTION_STR = "Endpoint=sb://jcbugsystem.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RnKgBHavWXnydS3wUygMQaBT/b7/bXDTWFEjtd5P2zY="
    STANDARD_QUEUE_NAME = "standardqueue"
    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_sender(queue_name=STANDARD_QUEUE_NAME) as sender:
            message = ServiceBusMessage(msg)
            sender.send_messages(message)
