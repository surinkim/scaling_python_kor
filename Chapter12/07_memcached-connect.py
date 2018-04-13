from pymemcache.client import base

# memcached는 이미 동작 중이어야 한다.
client = base.Client(('localhost', 11211))
client.set('some_key', 'some_value')
result = client.get('some_key')
print(result) # 'some_value' 출력