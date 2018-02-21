import threading


def print_something(something):
    print(something)


t = threading.Thread(target=print_something, args=("hello",))
t.start()
print("thread started")
t.join()
