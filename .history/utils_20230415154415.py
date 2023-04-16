from datetime import datetime

start = "2023-04-15 15:41:16.584727"
end = "2023-04-15 15:41:16.701895"


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    print (end - start)

time_diff(start, end)