import os
from time import sleep
import random

from dramatiq.brokers.rabbitmq import RabbitmqBroker
random.seed(10)

import dramatiq

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first_consumer(text):
    count = len(text.split(" "))
    print(f"There are {count} words")


@dramatiq.actor()
def second_consumer(text):
    count = len(text.split(" "))
    print(f"There are {count} words")


if __name__ == "__main__":
    array = []
    first_consumer.send("http://example.com")