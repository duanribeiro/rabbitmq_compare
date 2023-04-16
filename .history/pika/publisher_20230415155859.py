import json

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()



if __name__ == "__main__":
    for i in range(1000):
        channel.basic_publish(
            exchange='message',
            routing_key='example.text',
            body=i,
        )