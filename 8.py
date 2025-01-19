"""
    Lock
    safe
    Dead Lock
"""

from multiprocessing import Process, Lock, RLock, Semaphore, current_process
from time import sleep, perf_counter

lock = RLock()
lock2 = Semaphore(value=3)

#
# def add(num):
#     with lock:
#         subtract(num)
#         for _ in range(100000):
#             num += 1
#
#
# def subtract(num):
#     with lock:
#         for _ in range(100000):
#             num -= 1
#
#
# num = 0

num = 0


def add():
    global num
    lock.acquire()
    print(current_process().name)
    sleep(2)
    num += 1
    lock.release()


if __name__ == '__main__':
    p1 = Process(target=add())
    p2 = Process(target=add())
    p3 = Process(target=add())
    p4 = Process(target=add())
    p5 = Process(target=add())
    p6 = Process(target=add())

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    print('Done!')
    print(num)
