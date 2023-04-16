import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('amqp://guest:guest@localhost:5672'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')