import uuid

from tooz import coordination

# UUID를 사용해서 고유 식별자 생성
identifier = str(uuid.uuid4())
# Coordinator 객체 얻음
c = coordination.get_coordinator(
    "etcd3://localhost", identifier)
# Coordinator 시작(연결 시작)
c.start(start_heart=True)

lock = c.get_lock(b"name_of_the_lock")
# 락 획득 및 해제
assert lock.acquire() is True
assert lock.release() is True

# 획득하지 않은 락은 해제 못함
assert lock.release() is False

assert lock.acquire() is True
#블록 하지 않고 락 획득 시도(실패해도 바로 알 수 있음.)
assert lock.acquire(blocking=False) is False
# 락 획득 시도 시에 5초간 대기
assert lock.acquire(blocking=5) is False
assert lock.release() is True

# 프로그램이 끝나면 Coordinator도 종료
c.stop()