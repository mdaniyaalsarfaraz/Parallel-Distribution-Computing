import threading
import time
import random

# ---- Function to simulate some work ----
def do_something(count, out_list):
    """Simulates a task by generating random numbers."""
    for _ in range(count):
        out_list.append(random.random())

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
if __name__ == "__main__":
    size = 1000000   # work per thread
    threads = 5      # number of threads
    jobs = []

    print("Starting multithreading example...")
    start_time = time.time()

    for i in range(threads):
        out_list = []
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print("\nList processing complete.")
    print("Multithreading time =", end_time - start_time, "seconds")

    # ---- Run calculator after threads complete ----
    calculator()
