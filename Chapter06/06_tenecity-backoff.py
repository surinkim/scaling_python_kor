import tenacity
import random


def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")


@tenacity.retry(
wait=tenacity.wait_exponential(multiplier=0.5, max=30, exp_base=2),
)
def do_something_and_retry():
    do_something()


do_something_and_retry()