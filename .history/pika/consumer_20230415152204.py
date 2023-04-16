from datetime import datetime

from asynchronous_consumer import ExampleConsumer

from pika.exchange_type import ExchangeType


class CreateRPSConsumer(ExampleConsumer):
    EXCHANGE = 'pika'
    EXCHANGE_TYPE = ExchangeType.direct
    QUEUE = 'pika'
    ROUTING_KEY = 'pika'

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        time = datetime.now() - datetime.strptime(base_time, "%H:%M:%S")
        print(f"{id},{attempt},{time.seconds}")
        self.acknowledge_message(delivery_tag=basic_deliver.delivery_tag)


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="amqp://guest:guest@localhost:5672"))
    channel = connection.channel()

    channel.queue_declare(queue='text')

    channel.basic_publish(exchange='',
                    routing_key='example.text',
                    body=1)
    connection.close()

    consumer = CreateRPSConsumer()
    consumer.run()
