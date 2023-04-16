
import os
from datetime import datetime

import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from utils import bubble_sort
broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

@dramatiq.actor()
@profile
def consumer(id, array):
    print(f"{datetime.now()}")

if __name__ == "__main__":
    for i in range(1000):
        consumer.send(id=1, array=[1,3,12,6,10,2])