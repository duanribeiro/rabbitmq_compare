from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
end = ""
memory_start = 
memory_end = 

time_diff(start, end)

# dramatiq
start = ""
end = ""
memory_start = 
memory_end = 
time_diff(start, end)
