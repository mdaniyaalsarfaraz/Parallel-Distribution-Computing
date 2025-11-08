import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait until all processes using the barrier reach this point
    now = time()
    with serializer:      # Ensure only one process prints at a time
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)  # Wait for 2 processes before continuing
    serializer = Lock()         # Lock for synchronized printing

    # Processes using the barrier
    Process(name='p1 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    Process(name='p2 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    # Processes without barrier
    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()

    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
