from datetime import datetime


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

# pika
start = "2023-04-15 15:46:41.485729"
end = "2023-04-15 15:46:41.485729"
time_diff(start, end)

# dramatiq
start = "2023-04-15 15:48:37.045305"
end = "2023-04-15 15:48:38.476704"
time_diff(start, end)


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp