import socket

#s = socket.socket(…)
#s.connect(…)
with open("file.txt", "r") as f:
    content = f.read()
s.send(content)
