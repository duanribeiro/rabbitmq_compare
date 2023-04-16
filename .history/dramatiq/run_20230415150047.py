
from datetime import datetime

from utils import bubble_sort

from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


base_time = datetime.now()

@dramatiq.actor()
def consumer(id, attempt):
    if attempt = 1:
        base_time = datetime.now()

    time = datetime.now() - base_time 
    print(f"{id},{attempt},{time.seconds}")
    if attempt < 10:
        consumer.send(id, attempt + 1)
    # sorted_array = bubble_sort(array=array)
    # print(sorted_array)



if __name__ == "__main__":
    for i in range(50):
        consumer.send(id=i, attempt=1)