from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 13:38:43.720935"
memory_start = 17395712

end = "2023-04-16 13:39:03.399398"
memory_end = 17612800

time_diff(start, end)
print(memory_end - memory_start)

# dramatiq
start = "2023-04-16 13:40:45.486189"
memory_start =  

end = "2023-04-16 13:41:56.574486"
memory_end = 24088576
time_diff(start, end)
print(memory_end - memory_start)
