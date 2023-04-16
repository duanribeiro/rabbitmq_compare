
from datetime import datetime

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

@dramatiq.actor()
def consumer(id):
    print(f"{id}, {datetime.now()}")
    if attempt < 100:
        consumer.send(id, attempt + 1, base_time)