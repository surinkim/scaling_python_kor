import threading
import time

import cotyledon


class PrinterService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()

    def run(self):
        while not self._shutdown.is_set():
            print("Doing stuff")
            time.sleep(1)

    def terminate(self):
        self._shutdown.set()


# manager 생성
manager = cotyledon.ServiceManager()
# 2개의 PrinterService를 실행하기 위해 추가
manager.add(PrinterService, 2)
# manager에 추가된 작업을 모두 실행
manager.run()