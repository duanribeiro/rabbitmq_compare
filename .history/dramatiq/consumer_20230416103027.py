
import os
from datetime import datetime

import psutil

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from utils import bubble_sort

broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-15 15:46:41.485729"
end = "2023-04-15 15:46:41.485729"
time_diff(start, end)

# dramatiq
start = "2023-04-15 15:48:37.045305"
end = "2023-04-15 15:48:38.476704"
time_diff(start, end)


# Python program for implementation of Bubble Sort

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
@profile
def consumer(id, array):
    bubble_sort(array=array)
    print(f"{datetime.now()}")

if __name__ == "__main__":
    for i in range(1000):
        consumer.send(id=1, array=[1,3,12,6,10,2])