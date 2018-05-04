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
        page = requests.get("http://httpbin.org/uuid")
        cache[URL] = page.text
        print(page.text)
    time.sleep(1)