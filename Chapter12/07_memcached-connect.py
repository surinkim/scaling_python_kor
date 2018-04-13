from pymemcache.client import base

# memcached를 먼저 시작해야 한다.
client = base.Client(('localhost', 11211))
client.set('some_key', 'some_value')
result = client.get('some_key')
print(result) # 'some_value' 출력