import redis

r = redis.Redis()
r.publish("chatroom", "hello world")