import time

import fasteners


lock = fasteners.InterProcessLock("/tmp/mylock")
with lock:
    print("Access locked")
    time.sleep(1)