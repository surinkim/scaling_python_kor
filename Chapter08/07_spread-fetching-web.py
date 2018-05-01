import itertools
import uuid

import requests
from tooz import coordination


class URL(str):
    def __tooz_hash__(self):
        # URL을 고유 식별자로 사용한다.
        return self.encode()

urls_to_fetch = [
    URL("https://httpbin.org/bytes/%d" % n)
    for n in range(100)
]

GROUP_NAME = b"fetcher"
MEMBER_ID = str(uuid.uuid4()).encode('ascii')

# Coordinator 객체 얻음
c = coordination.get_coordinator("memcached://localhost", MEMBER_ID)
# Coordinator 시작(연결 시작)
c.start(start_heart=True)

# 파티션 그룹에 참가
p = c.join_partitioned_group(GROUP_NAME)

try:
    for url in itertools.cycle(urls_to_fetch):
        # 멤버십 변경이 없는지 확인
        c.run_watchers()
        # print("%s -> %s" % (url, p.members_for_object(url)))
        if p.belongs_to_self(url):
            try:
                r = requests.get(url)
            except Exception:
                # 에러가 발생하면
                # 단순히 다음 아이템으로 이동
                pass
            else:
                print("%s: fetched %s (%d)"
                     % (MEMBER_ID, r.url, r.status_code))
finally:
    # 그룹 나가기
    c.leave_group(GROUP_NAME).get()