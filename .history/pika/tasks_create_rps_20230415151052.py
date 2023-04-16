import json

from pika.exchange_type import ExchangeType

from asynchronous_consumer import ExampleConsumer

LOGGER = StructuredLogger(__name__)


class CreateRPSConsumer(AsynchronousConsumer):
    EXCHANGE = "rps-create-exchange"
    EXCHANGE_TYPE = ExchangeType.direct
    QUEUE = "rps-create"
    ROUTING_KEY = "rps-create"
    DEAD_LETTER_EXCHANGE = "rps-create-dlx"
    DEAD_LETTER_EXCHANGE_TYPE = ExchangeType.direct
    DEAD_LETTER_QUEUE = "rps-create-dlq"
    DEAD_LETTER_ROUTING_KEY = "rps-create-dlq"

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
