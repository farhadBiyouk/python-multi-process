"""
    terminate, kill, exitcode
"""

from multiprocessing import Process
from time import sleep, perf_counter


def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


if __name__ == '__main__':
    start = perf_counter()

    p1 = Process(target=show, args=('one',))
    p2 = Process(target=show, args=('two',))

    p1.start()
    p2.start()

    print(p1.is_alive())
    print(p2.is_alive())
    print('**********************')

    p1.kill()
    print('alan injam')
    p1.join()
    print('hala injam')
    print(p1.is_alive())
    print(p2.is_alive())
    p2.join()
    print('**********************')
    print(p1.is_alive())
    print(p2.is_alive())

    print('Done!')
    print(p1.exitcode)
    print(p2.exitcode)
    end = perf_counter()

    print(round(end - start))
