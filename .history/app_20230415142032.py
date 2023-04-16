import os
from time import sleep

from dramatiq.brokers.rabbitmq import RabbitmqBroker
from faker import Faker

import dramatiq

os.environ['dramatiq_queue_prefetch'] = '100' 

class MyBatchMiddleware(dramatiq.Middleware):
    def after_process_message(self, broker, message, *, result=None, exception=None):
        print(message)


fake = Faker()

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


@dramatiq.actor()
def first(text):
    count = len(text.split(" "))
    print(f"There are {count} words")



if __name__ == "__main__":
    for i in range(10):
        message = count.send(fake.address())