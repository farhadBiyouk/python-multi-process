"""
    Pool
"""
from multiprocessing import Process, Pool
from time import sleep, perf_counter


def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


if __name__ == '__main__':
    names = ['one', 'two', 'three', 'four']

    pool = Pool(processes=2)
    pool.map(show, names)
    pool.close()
    pool.join()
