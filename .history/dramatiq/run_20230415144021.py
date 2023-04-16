
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from datetime import datetime
import dramatiq
from utils import bubble_sort

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first_consumer(array):
    print(f"first_consumer: {datetime.now()}")
    second_consumer.send(array)
    # sorted_array = bubble_sort(array=array)
    # print(sorted_array)


@dramatiq.actor()
def second_consumer(text):
    print(f"second_consumer: {datetime.now()}")


if __name__ == "__main__":
    array = [1, 5, 2, 8, 3, 4, 7, 6]
    first_consumer.send(array)