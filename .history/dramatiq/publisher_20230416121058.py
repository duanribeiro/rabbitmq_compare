from consumer import consumer

if __name__ == "__main__":
    TOTAL_MESSAGES = 1000
    array = [10, 22, 32, 2, 5 ,34, 9 , 0, 13, 22]
    for i in range(TOTAL_MESSAGES):
        consumer.send(i=i, array=)