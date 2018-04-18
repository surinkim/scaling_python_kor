import socket

#s = socket.socket(…)
#s.connect(…)
data = b"a" * (1024 * 100000) 
while data:
    sent = s.send(data)
    data = data[sent:]