import threading
import time


stop = threading.Event()


def background_job():
    while not stop.is_set():
        print("I'm still running!")
        stop.wait(0.1)


t = threading.Thread(target=background_job)
t.start()
print("thread started")
time.sleep(1)
stop.set()
t.join()