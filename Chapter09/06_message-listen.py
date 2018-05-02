import redis

r = redis.Redis()
p = r.pubsub()
p.subscribe("chatroom")
for message in p.listen():
    print(message)