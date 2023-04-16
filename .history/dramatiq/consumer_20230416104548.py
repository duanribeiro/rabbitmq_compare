
import os
from datetime import datetime

import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)


def bubbleSort(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return

@dramatiq.actor()
def consumer(id, array):
	process = psutil.Process()
	pid = os.getpid()
	bubbleSort(arr=array)
	print(f"PID: {pid}")
	print(process.memory_info().rss)

	consumer2.send(id=1, array=[1, 5, 2, 8, 3, 4, 7, 6])

@dramatiq.actor()
def consumer2(id, array):
	process = psutil.Process()
	pid = os.getpid()
	bubbleSort(arr=array)
	print(f"PID: {pid}")
	print(process.memory_info().rss)