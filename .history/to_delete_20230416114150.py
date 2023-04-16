from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 11:37:11.052811"
end = "2023-04-16 11:37:12.519839"
memory_start = 17408000
memory_end = 17526784

time_diff(start, end)

# dramatiq
start = "2023-04-16 11:40:50.077970"
end = "2023-04-16 11:40:55.541168"
memory_start = 23764992
memory_end = 24064000
time_diff(start, end)
