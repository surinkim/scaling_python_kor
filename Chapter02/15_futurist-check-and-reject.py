import futurist
from futurist import rejection
import random


def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


with futurist.ThreadPoolExecutor(
        max_workers=8,
        check_and_reject=rejection.reject_when_reached(16)) as executor:
    futures = [executor.submit(compute) for _ in range(20)]
    print(executor.statistics)

results = [f.result() for f in futures]
print(executor.statistics)

print("Results: %s" % results)