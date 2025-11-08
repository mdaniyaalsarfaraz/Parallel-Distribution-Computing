from threading import Thread
from queue import Queue
import time
import random

# ===================== CALCULATOR =====================
def calculator():
    print("\n=== CALCULATOR ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input! Numbers only.")

# ===================== THREADING WITH QUEUE =====================
class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(1, 100)
            self.queue.put(item)
            print(f'Producer notify: item {item} appended to queue by {self.name}')
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:  # Stop signal
                break
            print(f'Consumer notify: item {item} popped from queue by {self.name}')
            self.queue.task_done()
            time.sleep(0.5)

# ===================== MAIN =====================
if __name__ == "__main__":
    # Run Calculator
    calculator()

    # Run Threading Queue Demo
    print("\n=== THREADING WITH QUEUE DEMO ===")
    queue = Queue()

    producer = Producer(queue)
    consumers = [Consumer(queue) for _ in range(3)]

    producer.start()
    for c in consumers:
        c.start()

    producer.join()

    # Stop consumers gracefully
    for _ in consumers:
        queue.put(None)
    for c in consumers:
        c.join()

    print("Queue demo complete.")
