import os
import socket
import unittest


class TestWithMemcached(unittest.TestCase):
    def setUp(self):
        super(TestWithMemcached, self).setUp()
        if not os.getenv("PIFPAF_MEMCACHED_URL"):
            self.skipTest("Memcached is not running")

    def test_connect(self):
        s = socket.socket()
        s.connect(("localhost", int(os.getenv("PIFPAF_MEMCACHED_PORT"))))
