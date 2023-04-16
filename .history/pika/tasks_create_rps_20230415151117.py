import json

from pika.exchange_type import ExchangeType

from asynchronous_consumer import ExampleConsumer


class CreateRPSConsumer(ExampleConsumer):
    EXCHANGE = 'message'
    EXCHANGE_TYPE = ExchangeType.topic
    QUEUE = 'text'
    ROUTING_KEY = 'example.text'

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        print
        self.acknowledge_message(delivery_tag=basic_deliver.delivery_tag)


if __name__ == "__main__":
    consumer = CreateRPSConsumer()
    consumer.run()
