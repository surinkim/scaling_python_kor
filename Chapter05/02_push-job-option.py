import time

from rq import Queue
from redis import Redis
import requests

q = Queue(name="http", connection=Redis())

job = q.enqueue(requests.get, "http://httpbin.org/delay/1",
    ttl=60, result_ttl=300)
# URL을 가져오는 동안, 다른 작업을 할 수 있다.
# 결과가 준비될 때까지 대기한다.
while job.result is None:
    time.sleep(1)

print(job.result)