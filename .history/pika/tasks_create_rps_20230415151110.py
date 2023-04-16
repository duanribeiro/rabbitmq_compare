import json

from pika.exchange_type import ExchangeType

from asynchronous_consumer import ExampleConsumer


class CreateRPSConsumer(ExampleConsumer):
    EXCHANGE = 'message'
    EXCHANGE_TYPE = ExchangeType.topic
    QUEUE = 'text'
    ROUTING_KEY = 'example.text'

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        LOGGER.info(
            origin="on_message",
            message=f"Received message #{basic_deliver.delivery_tag} "
            + f"from {properties.app_id}: {body}",
        )

        sls_message = json.loads(body.decode())["sls_message"]
        controller = RPSController()
        controller.create_rps(sls_message=sls_message)
        self.acknowledge_message(delivery_tag=basic_deliver.delivery_tag)


if __name__ == "__main__":
    consumer = CreateRPSConsumer()
    consumer.run()
