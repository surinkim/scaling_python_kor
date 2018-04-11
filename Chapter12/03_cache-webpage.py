import time

import cachetools
import requests


cache = cachetools.TTLCache(maxsize=5, ttl=5)
URL = "http://httpbin.org/uuid"
while True:
    try:
        print(cache[URL])
    except KeyError:
        print("Paged not cached, fetching")
        cache[URL] = page = requests.get("http://httpbin.org/uuid")
        print(page)
    time.sleep(1)