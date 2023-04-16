import json

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=pika.PlainCredentials('guest', 'guest')
    )
)
channel = connection.channel()

TOTAL_MESSAGES = 10000
ARRAY = [
    10, 22, 32, 2, 5 ,34, 9 , 0, 13, 22,
    11, 23, 33, 3, 6 ,35, 10, 1, 14, 23,
    12, 24, 34, 4, 7 ,36, 11, 2, 15, 24,
    13, 25, 35, 5, 8 ,37, 12, 3, 16, 25,
    14, 26, 36, 6, 9 ,38, 13, 4, 17, 26,
    15, 27, 37, 7, 10, 39, 14, 5, 18, 27,
    16, 28, 38, 8, 11, 40, 15, 6, 19, 28,
    17, 29, 39, 9, 12, 41, 16, 7, 20, 29,
    18, 30, 40, 10, 13, 42, 17, 8, 21, 30,
    19, 31, 41, 11, 14, 43, 18, 9, 22, 31,
]

if __name__ == "__main__":
    for i in range(TOTAL_MESSAGES):
        channel.basic_publish(
            exchange='pika_exchange',
            routing_key='pika',
            body=json.dumps(ARRAY),
        )