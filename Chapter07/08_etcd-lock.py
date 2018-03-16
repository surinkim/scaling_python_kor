import etcd3

client = etcd3.client()
lock = client.lock("foobar")
lock.acquire()
try:
    print("do something")
finally:
    lock.release()