from datetime import datetime

from consumer import consumer

if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        consumer.send(id=i, array=[10, 22, 32, 2, 5 ,34, 9 , 0,13, 22])