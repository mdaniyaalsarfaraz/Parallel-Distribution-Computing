import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Producer: item {item} appended to queue by {self.name}")
            print(f"Queue size: {self.queue.qsize()}")
            time.sleep(1)

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Consumer: queue is empty, stopping")
                break
            item = self.queue.get()
            print(f"Consumer: item {item} popped by {self.name}")
            time.sleep(2)  # simulate processing time

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    producer_process = Producer(queue)
    consumer_process = Consumer(queue)

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("All processes finished.")
