# Combined Multiprocessing Example:
# - Spawning Multiple Processes
# - Calculator Logic with Background & Non-background Processes
# Chapter 3: Process-Based Parallelism

import multiprocessing
import time
from datetime import datetime

# --- Function 1: Simple Spawned Process ---
def myFunc(i):
    print(f"[{datetime.now()}] Calling myFunc from process no: {i}")
    for j in range(i):
        print(f"Output from myFunc({i}) → {j}")
    time.sleep(0.5)
    print(f"Process {i} finished.\n")


# --- Function 2: Calculator Example ---
def calculator():
    name = multiprocessing.current_process().name
    print(f"\nStarting {name} at {datetime.now()}")

    if name == 'background_process':
        for i in range(0, 5):
            print(f"{name} ---> {i}")
            time.sleep(0.3)
    else:
        for i in range(5, 10):
            print(f"{name} ---> {i}")
            time.sleep(0.3)

    print(f"Exiting {name} at {datetime.now()}\n")


if __name__ == '__main__':
    print("\n=== Spawning Processes Example ===\n")
    processes = []

    # Spawn multiple processes for myFunc
    for i in range(6):
        p = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\n=== Calculator Example (Background + Non-Background) ===\n")

    # Create calculator processes
    background_process = multiprocessing.Process(name='background_process', target=calculator)
    background_process.daemon = True  # Background process (dies when main ends)

    no_background_process = multiprocessing.Process(name='NO_background_process', target=calculator)
    no_background_process.daemon = False  # Normal process

    # Start both calculator processes
    background_process.start()
    no_background_process.start()

    # Wait for non-daemon process to complete
    no_background_process.join()

    print("\nAll processes completed successfully!")
