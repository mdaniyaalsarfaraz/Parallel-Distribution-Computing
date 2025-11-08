import threading
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

# ===================== LOCK EXAMPLE =====================
lock = threading.Lock()
def locked_task(name):
    with lock:
        print(f"{name} acquired the lock")
        time.sleep(1)
        print(f"{name} released the lock")

# ===================== RLOCK EXAMPLE =====================
class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(box, items):
    while items:
        box.add()
        time.sleep(0.5)
        items -= 1

def remover(box, items):
    while items:
        box.remove()
        time.sleep(0.5)
        items -= 1

# ===================== EVENT EXAMPLE =====================
items_list = []
event = threading.Event()

class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            item = random.randint(0, 100)
            items_list.append(item)
            print(f"Producer produced: {item}")
            event.set()
            event.clear()

class Consumer(threading.Thread):
    def run(self):
        for _ in range(5):
            event.wait()
            while items_list:
                item = items_list.pop(0)
                print(f"Consumer consumed: {item}")
            event.clear()

# ===================== BARRIER EXAMPLE =====================
num_runners = 3
finish_line = threading.Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner(name):
    time.sleep(random.randint(1, 3))
    print(f"{name} reached the barrier")
    finish_line.wait()

# ===================== MAIN =====================
if __name__ == "__main__":
    # Calculator
    calculator()

    # Lock demo
    print("\n=== LOCK DEMO ===")
    t1 = threading.Thread(target=locked_task, args=("Thread1",))
    t2 = threading.Thread(target=locked_task, args=("Thread2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # RLock demo
    print("\n=== RLOCK DEMO ===")
    box = Box()
    t3 = threading.Thread(target=adder, args=(box, 5))
    t4 = threading.Thread(target=remover, args=(box, 3))
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print(f"Final total items in box: {box.total_items}")

    # Event demo
    print("\n=== EVENT DEMO ===")
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

    # Barrier demo
    print("\n=== BARRIER DEMO ===")
    threads = []
    for name in runners:
        threads.append(threading.Thread(target=runner, args=(name,)))
        threads[-1].start()
    for t in threads:
        t.join()
    print("All runners crossed the barrier!")
