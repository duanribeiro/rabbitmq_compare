from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 13:24:58.297106"
memory_start = 17440768

end = "2023-04-16 13:25:06.328981"
memory_end = 17633280

time_diff(start, end)
print(memory_end - memory_start)

# dramatiq
start = "2023-04-16 13:26:11.640880"
memory_start = 23736320

end = "2023-04-16 13:27:08.898753"
memory_end = 23990272
time_diff(start, end)
print(memory_end - memory_start)
