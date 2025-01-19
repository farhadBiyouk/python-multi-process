from time import sleep, perf_counter
from multiprocessing import Process


def show(name, delay):
    print(f'Starting {name}')
    sleep(delay)
    print(f'Finishing {name}')


class ShowProcess(Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


if __name__ == '__main__':
    start = perf_counter()
    p1 = ShowProcess('one', 3)
    p2 = ShowProcess('two', 5)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = perf_counter()

    print(round(end - start))
