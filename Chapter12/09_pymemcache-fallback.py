from pymemcache.client import base
from pymemcache import fallback


def do_some_query():
    # 실제로는 데이터베이스나 REST API로 원격에서 데이터를 가져온다고 가정함.
    return 42


# 'ignore_exc=True'로 설정해서 캐시 누락을 처리할 수 있도록 한다.
# 새 캐시에 데이터가 채워지면, 이전 캐시 서버를 중지할 수 있다.
old_cache = base.Client(('localhost', 11211), ignore_exc=True)
new_cache = base.Client(('localhost', 11212))

client = fallback.FallbackClient((new_cache, old_cache))

result = client.get('some_key')
if result is None:
    # 캐시에 없는 데이터는 원본 소스에서 가져와야 한다.
    result = do_some_query()
    # 다음 조회를 위해 결과를 캐시한다.
    client.set('some_key', result)
print(result)
