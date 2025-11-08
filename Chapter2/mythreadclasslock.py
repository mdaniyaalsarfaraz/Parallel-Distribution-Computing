import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

# ---- Custom Thread Class ----
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the Lock
        threadLock.acquire()      
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}\n")
        time.sleep(self.duration)
        print(f"---> {self.name} over\n")
        # Release the Lock
        threadLock.release()

# ---- Simple Calculator ----
def calculator():
    print("\nSimple Calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid input!")

# ---- Main Program ----
def main():
    start_time = time.time()

    # Thread Creation
    threads = [MyThreadClass(f"Thread#{i+1}", randint(1,10)) for i in range(9)]

    # Thread Running
    for thread in threads:
        thread.start()

    # Thread Joining
    for thread in threads:
        thread.join()

    print("All threads completed.")

    # Execution Time
    print(f"--- {time.time() - start_time:.2f} seconds ---")

    # Run Calculator
    calculator()

if __name__ == "__main__":
    main()
