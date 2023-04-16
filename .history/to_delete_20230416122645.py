from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
memory_start = 

end = "2023-04-16 12:25:30.923449"
memory_end = 17502208

time_diff(start, end)

# dramatiq
start = ""
memory_start = 

end = ""
memory_end = 
time_diff(start, end)
