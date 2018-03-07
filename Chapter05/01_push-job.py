import time

from rq import Queue
from redis import Redis

q = Queue(connection=Redis())

job = q.enqueue(sum, [42, 43])
# 결과가 준비될 때까지 대기한다.
while job.result is None:
    time.sleep(1)

print(job.result)
