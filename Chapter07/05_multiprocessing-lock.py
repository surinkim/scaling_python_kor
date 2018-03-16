import multiprocessing
import time


stdout_lock = multiprocessing.Lock()


def print_cat():
    # 조금 기다려서 랜덤한 결과가 나오도록 한다.
    time.sleep(0.1)
    with stdout_lock:
        print(" /\\_/\\")
        print("( o.o )")
        print(" > ^ <")


with multiprocessing.Pool(processes=3) as pool:
    jobs = []
    for _ in range(5):
        jobs.append(pool.apply_async(print_cat))
    for job in jobs:
        job.wait()