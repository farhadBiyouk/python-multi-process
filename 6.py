"""
    Queue
"""

from multiprocessing import Process, Queue
from time import sleep, perf_counter

numbers = []


def fun1(queue):
    num = queue.get()
    num.extend([1, 2, 3])
    queue.put(num)
    print(num)


def fun2(queue):
    num = queue.get()
    num.extend([4, 5, 6])
    queue.put(num)
    print(num)


if __name__ == '__main__':
    qs = Queue()

    qs.put(numbers)
    p1 = Process(target=fun1, args=(qs,))
    p2 = Process(target=fun2, args=(qs,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!')

    print(qs.get())
