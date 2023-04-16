import json
from datetime import datetime

from asynchronous_consumer import ExampleConsumer

from pika.exchange_type import ExchangeType


class CreateRPSConsumer(ExampleConsumer):
    EXCHANGE = 'pika'
    EXCHANGE_TYPE = ExchangeType.direct
    QUEUE = 'pika'
    ROUTING_KEY = 'pika'

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        body = json.loads(body.decode())
        
        time = datetime.now() - datetime.strptime(base_time, "%H:%M:%S")
        print(f"{id},{attempt},{time.seconds}")
        self.acknowledge_message(delivery_tag=basic_deliver.delivery_tag)


if __name__ == "__main__":
    consumer = CreateRPSConsumer()
    consumer.run()
