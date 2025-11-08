import multiprocessing
import time

def foo():
    print('Starting function')
    for i in range(10):
        print('-->%d' % i)
        time.sleep(1)
    print('Finished function')

if __name__ == '__main__':
    # Create the process
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())

    # Start the process
    p.start()
    print('Process running:', p, p.is_alive())

    # Terminate the process before it finishes
    p.terminate()
    print('Process terminated:', p, p.is_alive())

    # Wait for process to fully exit
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
