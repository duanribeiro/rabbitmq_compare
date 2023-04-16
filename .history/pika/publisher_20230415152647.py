import json
from datetime import datetime

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()



if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        channel.basic_publish(
            exchange='message',
            routing_key='hello',
            body=json.dumps({"id": i, "attempt": 1, "base_time": base_time})
        )