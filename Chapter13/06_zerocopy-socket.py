import socket

#s = socket.socket(…)
#s.connect(…)
data = b"a" * (1024 * 100000)
mv = memoryview(data)
while mv:
    sent = s.send(mv)
    mv = mv[sent:]