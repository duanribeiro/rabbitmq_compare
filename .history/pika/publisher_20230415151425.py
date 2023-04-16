connection = pika.BlockingConnection(pika.ConnectionParameters(host="amqp://guest:guest@localhost:5672"))
    channel = connection.channel()

    channel.queue_declare(queue='text')

    channel.basic_publish(exchange='',
                    routing_key='example.text',
                    body=1)
    connection.close()