from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = ""
memory_start = 

end = ""
memory_end = 

time_diff(start, end)
print(memory_end - memory_start)

# dramatiq
start = ""
memory_start =  

end = ""
memory_end = 
time_diff(start, end)
print(memory_end - memory_start)
