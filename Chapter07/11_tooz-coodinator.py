import uuid

from tooz import coordination

# UUID를 사용해서 고유 식별자 생성
identifier = str(uuid.uuid4())
# Coordinator 객체 얻음
c = coordination.get_coordinator(
    "etcd3://localhost", identifier)
# Coordinator 시작(연결 시작)
c.start(start_heart=True)
# 프로그램이 끝나면 Coordinator도 종료
c.stop()