
from datetime import datetime

from utils import bubble_sort

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def consumer(id, attempt):
    print(f"{attempt} | {id} | {datetime.now()}")
    consumer.send(id, array)
    if attempt < 10:
        consumer.send(id, attempt + 1)
    else:
        print("Done")
    # sorted_array = bubble_sort(array=array)
    # print(sorted_array)



if __name__ == "__main__":
    for i in range(10):
        consumer.send(id=i, attempt=1)