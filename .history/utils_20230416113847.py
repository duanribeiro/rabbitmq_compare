from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
end = "2023-04-16 11:37:12.519839"
memory_start = 
memory_end = 17526784

time_diff(start, end)

# dramatiq
start = ""
end = ""
memory_start = 17485824
memory_end = 17485824
time_diff(start, end)
