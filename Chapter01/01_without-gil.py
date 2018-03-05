import threading

x = []

def append_two(l):
    l.append(2)

threading.Thread(target=append_two, args=(x,)).start()

x.append(1)
print(x)
