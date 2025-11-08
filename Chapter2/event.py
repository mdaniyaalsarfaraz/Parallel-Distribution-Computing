import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()
stop_event = threading.Event()  # To stop the consumer gracefully

class Consumer(threading.Thread):
    def run(self):
        while not stop_event.is_set() or items:
            event.wait()  # Wait for producer
            while items:
                item = items.pop(0)  # Pop first item
                logging.info(f'Consumer notify: {item} popped by {self.name}')
            event.clear()

class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info(f'Producer notify: item {item} appended by {self.name}')
            event.set()  # Notify consumer
        stop_event.set()  # Signal consumer to stop

if __name__ == "__main__":
    producer = Producer(name="ProducerThread")
    consumer = Consumer(name="ConsumerThread")

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    logging.info("All threads completed.")
