from consumer import consumer

if __name__ == "__main__":
    TOTAL_MESSAGES = 1000
    array = []
    for i in range(TOTAL_MESSAGES):
        consumer.send(i=i, array=)