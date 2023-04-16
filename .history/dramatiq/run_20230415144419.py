
from datetime import datetime

from utils import bubble_sort

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first_consumer(id, array):
    print(f"first_consumer | {id} | {datetime.now()}")
    second_consumer.send(id, array)
    # sorted_array = bubble_sort(array=array)
    # print(sorted_array)


@dramatiq.actor()
def second_consumer(id, array):
    print(f"second_consumer | {id} | {datetime.now()}")


if __name__ == "__main__":
    for i in range(10):
        first_consumer.send(i, array)