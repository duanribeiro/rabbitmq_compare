from consumer import consumer

if __name__ == "__main__":
    TOTAL_MESSAGES = 1000
    for i in range(1000):
        consumer.send(i=i, array=[10, 22, 32, 2, 5 ,34, 9 , 0, 13, 22])