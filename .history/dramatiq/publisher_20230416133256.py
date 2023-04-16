from consumer import consumer

if __name__ == "__main__":
    TOTAL_MESSAGES = 1000
    ARRAY = [
        10, 22, 32, 2, 5 ,34, 9 , 0, 13, 22,
        11, 23, 33, 3, 6 ,35, 10, 1, 14, 23,
        12, 24, 34, 4, 7 ,36, 11, 2, 15, 24,
        13, 25, 35, 5, 8 ,37, 12, 3, 16, 25,
        14, 26, 36, 6, 9 ,38, 13, 4, 17, 26,
        15, 27, 37, 7, 10, 39, 14, 5, 18, 27,
        16, 28, 38, 8, 11, 40, 15, 6, 19, 28,
        

    ]

    for i in range(TOTAL_MESSAGES):
        consumer.send(i=i, array=ARRAY)