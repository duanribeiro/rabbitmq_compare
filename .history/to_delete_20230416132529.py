from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
memory_start = 

end = ""
memory_end = 

time_diff(start, end)
print(memory_end - memory_start)

# dramatiq
start = "2023-04-16 13:19:37.444861"
memory_start = 23728128 

end = "2023-04-16 13:19:42.698214"
memory_end = 24027136
time_diff(start, end)
print(memory_end - memory_start)
