import threading
import logging
import random
import time

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

# ===================== SEMAPHORE DEMO =====================
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)
item = 0

def consumer():
    logging.info('Consumer waiting for item...')
    semaphore.acquire()
    logging.info(f'Consumer got item: {item}')

def producer():
    global item
    time.sleep(random.randint(1, 3))
    item = random.randint(1, 100)
    logging.info(f'Producer produced item: {item}')
    semaphore.release()

# ===================== MAIN =====================
if __name__ == "__main__":
    # Run Calculator
    calculator()

    # Run Semaphore Demo
    print("\n=== SEMAPHORE DEMO ===")
    consumers = [threading.Thread(target=consumer) for _ in range(3)]
    producers = [threading.Thread(target=producer) for _ in range(3)]

    # Start all threads
    for c in consumers:
        c.start()
    for p in producers:
        p.start()

    # Join all threads
    for c in consumers:
        c.join()
    for p in producers:
        p.join()

    print("Semaphore demo complete.")
