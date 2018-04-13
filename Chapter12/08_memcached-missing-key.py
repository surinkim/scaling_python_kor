from pymemcache.client import base


def do_some_query():
    # 실제로는 데이터베이스나 REST API로 원격에서 데이터를 가져온다고 가정함.
    return 42


# memcached는 이미 동작 중이어야 한다.
client = base.Client(('localhost', 11211))
result = client.get('some_key')
if result is None:
    # 캐시에 없는 데이터는 원본 소스에서 가져와야 한다.
    result = do_some_query()
    # 다음 조회를 위해 결과를 캐시한다.
    client.set('some_key', result)
print(result)