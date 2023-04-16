from datetime import datetime

import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()



if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        channel.basic_publish(
            exchange='message',
            routing_key='hello',
            body=json.loads({"id": i, "attempt": 1, "base_time": base_time}
        )