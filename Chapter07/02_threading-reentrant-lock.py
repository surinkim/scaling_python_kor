import threading

rlock = threading.RLock()

with rlock:
    with rlock:
        print("Double acquired")