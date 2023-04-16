from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-16 13:34:16.660722"
memory_start = 17494016

end = "2023-04-16 13:34:20.378714"
memory_end = 17571840

time_diff(start, end)
print(memory_end - memory_start)

# dramatiq
start = ""
memory_start =  

end = "2023-04-16 13:35:41.185017"
memory_end = 
time_diff(start, end)
print(memory_end - memory_start)
