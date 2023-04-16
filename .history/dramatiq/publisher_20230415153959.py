from datetime import datetime

from consumer import consumer

if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(10):
        consumer.send(id=i)