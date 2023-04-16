from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 11:37:11.052811"
memory_start = 17408000

end = "2023-04-16 12:25:30.923449"
memory_end = 17502208

time_diff(start, end)

# dramatiq
start = ""
memory_start = 

end = "2023-04-16 13:19:42.698214"
memory_end = 
time_diff(start, end)
