"""
    Process Pool Executor
"""

from multiprocessing import Process, cpu_count
from time import sleep
from concurrent.futures import ProcessPoolExecutor


def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


if __name__ == '__main__':
    names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    with ProcessPoolExecutor() as executor:
        executor.map(show, names)
    print('Done!')
