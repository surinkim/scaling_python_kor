import threading

stdout_lock = threading.Lock()


def print_something(something):
    with stdout_lock:
        print(something)


t = threading.Thread(target=print_something, args=("hello",))
t.daemon = True
t.start()
print_something("thread started")