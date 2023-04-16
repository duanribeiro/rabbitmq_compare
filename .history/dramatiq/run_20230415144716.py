
from datetime import datetime

from utils import bubble_sort

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first_consumer(id, attempt):
    print(f"first_consumer | {id} | {datetime.now()}")
    second_consumer.send(id, array)
    # sorted_array = bubble_sort(array=array)
    # print(sorted_array)



if __name__ == "__main__":
    for i in range(10):
        _consumer.send(id=i, attempt=1)