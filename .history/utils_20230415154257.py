from datetime import datetime

start = "2023-04-15 15:38:27.230068"
end = "2023-04-15 15:38:27.261039"


def time_diff(start, end):
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    return end - start

