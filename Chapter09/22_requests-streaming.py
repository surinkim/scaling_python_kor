import requests


# 'with'를 사용해서 응답 stream을 확실히 닫아서
# 연결을 다시 pool에 반환한다.
with requests.get('http://example.org', stream=True) as r:
    print(list(r.iter_content()))