from c
if __name__ == "__main__":
    base_time = datetime.now().strftime("%H:%M:%S")
    for i in range(100):
        consumer.send(id=i, attempt=1, base_time=base_time)