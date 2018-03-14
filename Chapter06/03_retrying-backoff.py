import time
import random


def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")


attempt = 0
while True:
    try:
        do_something()
    except:
        # 재시도 전에 2^attempt 동안 sleep
        time.sleep(2 ** attempt)
        attempt += 1
    else:
        break