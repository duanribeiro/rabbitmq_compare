from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
end = "2023-04-16 11:30:24.577164"
time_diff(start, end)

# dramatiq
start = ""
end = ""
time_diff(start, end)