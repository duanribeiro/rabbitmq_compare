from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-15 15:46:47.821194"
end = "2023-04-15 15:46:41.485729"
time_diff(start, end)

# dramatiq
start = ""
end = "2023-04-15 15:48:38.476704"
time_diff(start, end)