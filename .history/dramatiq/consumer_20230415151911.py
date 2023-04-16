
from datetime import datetime

from utils import bubble_sort

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


base_time = datetime.now()

@dramatiq.actor()
def consumer(id, attempt, base_time):
    time = datetime.now() - datetime.strptime(base_time, "%H:%M:%S")
    print(f"{id},{attempt},{time.seconds}")
    if attempt < 100:
        consumer.send(id, attempt + 1, base_time)



if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        consumer.send(id=i, attempt=1, base_time=base_time)