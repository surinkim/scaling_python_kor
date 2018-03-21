import sys
import time

from tooz import coordination

# client id와 group id가 인수로 전달됐는지 확인.
if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

# Coordinator 객체 얻음
c = coordination.get_coordinator(
    "memcached://localhost",
    sys.argv[1].encode())
# Coordinator 시작(연결 시작)
c.start(start_heart=True)

group = sys.argv[2].encode()

# 그룹 생성
try:
    c.create_group(group).get()
except coordination.GroupAlreadyExist:
    pass

# 그룹 참가
c.join_group(group).get()

# 그룹에 참가하거나 나갈 때 호출되도록
# print 함수를 등록한다.
c.watch_join_group(group, print)
c.watch_leave_group(group, print)

while True:
    c.run_watchers()
    time.sleep(2)

# 그룹 나가기
c.leave_group(group).get()

# 프로그램이 끝나면 Coordinator도 종료
c.stop()