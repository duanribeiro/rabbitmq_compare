from datetime import datetime

import psutil
from utils import bubbleSort

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(
	url="amqp://guest:guest@localhost:5672"
)
dramatiq.set_broker(broker)



@dramatiq.actor()
def consumer(i, array):
	process = psutil.Process()
	print(i)
	bubbleSort(arr=array)
	print(datetime.now())
	print(process.memory_info().rss)