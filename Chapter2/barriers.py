from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))  # simulate running
    print(f'{name} reached the barrier at: {ctime()}')
    finish_line.wait()
    print(f'{name} crossed the finish line at: {ctime()}')  # after barrier

def main():
    threads = []
    print('START RACE!!!!')
    for _ in range(num_runners):
        t = Thread(target=runner)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('Race over!')

if __name__ == "__main__":
    main()
