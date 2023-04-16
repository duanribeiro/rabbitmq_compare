
import os
from datetime import datetime

import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

@dramatiq.actor()
def consumer(id):
    # pid = os.getpid()
    # python_process = psutil.Process(pid)

    print(f"{datetime.now()}")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memory: {psutil.virtual_memory().percent}%")