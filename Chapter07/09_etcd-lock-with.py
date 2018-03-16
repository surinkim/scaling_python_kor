import etcd3

client = etcd3.client()
lock = client.lock("foobar")
with lock:
    print("do something")