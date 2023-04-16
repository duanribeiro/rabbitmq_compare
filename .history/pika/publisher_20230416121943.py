import json

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
    host='localhost',
    port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()



if __name__ == "__main__":
    for i in range(1000):
        channel.basic_publish(
            exchange='pika_exchange',
            routing_key='pika',
            body=json.dumps([10, 22, 32, 2, 5 ,34, 9 , 0, 13, 22]),
        )