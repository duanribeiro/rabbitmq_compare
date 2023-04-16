import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host=)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')