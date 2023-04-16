
from datetime import datetime

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
import psutil

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

@dramatiq.actor()
def consumer(id):
    print(f"{datetime.now()}")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memory: {psutil.virtual_memory().percent}%")
    