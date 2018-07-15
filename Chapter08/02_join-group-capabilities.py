import sys
import time

from tooz import coordination

# client id, group id 및 mood가 인수로 전달됐는지 확인.
if len(sys.argv) != 4:
    print("Usage: %s <client id> <group id> <mood>"
         % sys.argv[0])
    sys.exit(1)

# Coordinator 객체 얻음
c = coordination.get_coordinator(
    "etcd3://localhost",
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
c.join_group(
    group,
    capabilities={"mood": sys.argv[3]}
).get()

# 멤버 목록과 역량을 출력한다.
# API가 비동기 방식이므로, 역량을 얻기 위한 요청을
# 동시에 보내서 병렬로 실행되도록 한다.
get_capabilities = [
    (member, c.get_member_capabilities(group, member))
    for member in c.get_members(group).get()
]

for member, cap in get_capabilities:
    print("Member %s has capabilities: %s"
         % (member, cap.get()))

# 5초간 대기
time.sleep(5)

# 그룹 나가기
c.leave_group(group).get()

# 프로그램이 끝나면 Coordinator도 종료
c.stop()
