import sys
import time

from tooz import coordination

# client id와 group id가 인수로 전달됐는지 확인.
if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

# Coordinator 객체 얻음
c = coordination.get_coordinator(
    "etcd3://localhost",
    sys.argv[1].encode())
# Coordinator 시작(연결 시작)
c.start(start_heart=True)

group = sys.argv[2].encode()

# 파티션 그룹에 참가
p = c.join_partitioned_group(group)

print(p.members_for_object("foobar"))

# 5초간 대기
time.sleep(5)

# 그룹 나가기
c.leave_group(group).get()

# 프로그램이 끝나면 Coordinator도 종료
c.stop()