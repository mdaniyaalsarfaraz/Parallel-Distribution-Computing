import time
import threading
import multiprocessing
import random

# Function to simulate some work
def do_something(count, out_list):
    for _ in range(count):
        out_list.append(random.random())

# Function for calculator
def calculator(choice, num1, num2):
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

if __name__ == "__main__":
    # Threading example
    out_list = []
    NUM_WORKERS = 5
    SIZE = 1000000

    print("Starting threading example...")
    start = time.time()
    threads = []
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=do_something, args=(SIZE, out_list))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Threading time:", time.time() - start)

    # Multiprocessing
    print("\nStarting multiprocessing example...")
    out_list = multiprocessing.Manager().list()  # shared list for processes
    start = time.time()
    processes = []
    for i in range(NUM_WORKERS):
        p = multiprocessing.Process(target=do_something, args=(SIZE, out_list))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("Multiprocessing time:", time.time() - start)

    # Simple calculator
    print("\nSimple Calculator:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Run calculator in same process (no input errors)
    calculator(choice, num1, num2)
