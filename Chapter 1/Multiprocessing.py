import time
import multiprocessing
import random

# ---- Function that simulates some work ----
def do_something(count, out_list):
    """Simulates a CPU task by generating random numbers."""
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
    start_time = time.time()
    size = 10000000    # work per process
    procs = 10         # number of processes
    jobs = []

    print("Starting multiprocessing example...")

    for i in range(procs):
        out_list = []
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print("\nList processing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time, "seconds")

    # ---- Run calculator after multiprocessing ----
    calculator()
