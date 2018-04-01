import requests

session = requests.Session()
session.get("http://example.com")
# 이미 맺어진 연결을 재사용
session.get("http://example.com")