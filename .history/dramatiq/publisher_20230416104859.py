from datetime import datetime

from consumer import consumer

if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        consumer.send(id=1, array=[1, 5, 2, 8, 3, 4, 7, 6, 2, 8, 3, 4, 7, 6])