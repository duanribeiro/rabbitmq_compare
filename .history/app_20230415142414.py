import os
from time import sleep

from dramatiq.brokers.rabbitmq import RabbitmqBroker

import dramatiq

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first_consumer(text):
    count = len(text.split(" "))
    print(f"There are {count} words")



if __name__ == "__main__":
    for i in range(10):
        message = count.send(fake.address())