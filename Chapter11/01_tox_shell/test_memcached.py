import os
import socket
import unittest


class TestWithMemcached(unittest.TestCase):
    def setUp(self):
        super(TestWithMemcached, self).setUp()
        if not os.getenv("MEMCACHED_PID"):
            self.skipTest("Memcached is not running")

    def test_connect(self):
        s = socket.socket()
        s.connect(("localhost", 4526))