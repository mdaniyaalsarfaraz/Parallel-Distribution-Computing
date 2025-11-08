import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

def foo(synchronizer, serializer):
    name = multiprocessing.current_process().name

    # Wait until both processes reach this point
    synchronizer.wait()

    with serializer:
        print(f"\nStarting {name} at {datetime.fromtimestamp(time())}")

    if name == 'background_process':
        for i in range(0, 5):
            with serializer:
                print(f"{name} ---> {i}")
            sleep(0.5)
    else:
        for i in range(5, 10):
            with serializer:
                print(f"{name} ---> {i}")
            sleep(0.5)

    with serializer:
        print(f"Exiting {name} at {datetime.fromtimestamp(time())}\n")


if __name__ == '__main__':
    # Synchronization primitives
    synchronizer = Barrier(2)  # Wait for 2 processes to reach the barrier
    serializer = Lock()        # Lock to prevent print overlap

    # Create background and non-background processes
    background_process = Process(name='background_process', target=foo, args=(synchronizer, serializer))
    background_process.daemon = True  # Background/daemon process

    no_background_process = Process(name='NO_background_process', target=foo, args=(synchronizer, serializer))
    no_background_process.daemon = False

    # Start both processes
    background_process.start()
    no_background_process.start()

    # Wait for non-daemon process to finish (daemon ends automatically)
    no_background_process.join()
