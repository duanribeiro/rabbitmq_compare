from datetime import datetime
from utils import bubbleSort
import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = dramatiq.broker.rabbitmq.RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)



@dramatiq.actor()
def consumer(i, array):
	process = psutil.Process()
	print(i)
	bubbleSort(arr=array)
	print(datetime.now())
	print(process.memory_info().rss)


from datetime import datetime

import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from utils import bubbleSort

broker = dramatiq.broker.rabbitmq.RabbitmqBroker(
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