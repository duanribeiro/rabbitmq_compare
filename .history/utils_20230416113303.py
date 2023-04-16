from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 11:30:23.720019"
end = "2023-04-16 11:30:24.577164"
memory = 17485824
time_diff(start, end)

# dramatiq
start = ""
end = "2023-04-16 11:32:44.514838"
memory = 24039424
time_diff(start, end)
