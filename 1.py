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

    p1.join()
    p2.join()

    end = perf_counter()

    print(round(end - start))
