import time

import fasteners


@fasteners.interprocess_locked('/tmp/tmp_lock_file')
def locked_print():
    for i in range(10):
        print('I have the lock')
        time.sleep(0.1)


locked_print()