from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
end = ""
memory_start = 17408000
memory_end = 17526784

time_diff(start, end)

# dramatiq
start = ""
end = ""
memory_start = 23764992
memory_end = 24064000
time_diff(start, end)
