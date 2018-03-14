import tenacity
import random


def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")


tenacity.Retrying()(do_something)