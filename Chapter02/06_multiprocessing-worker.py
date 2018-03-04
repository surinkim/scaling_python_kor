import multiprocessing
import random


def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


# 8개의 워커를 시작한다.
pool = multiprocessing.Pool(processes=8)
print("Results: %s" % pool.map(compute, range(8)))