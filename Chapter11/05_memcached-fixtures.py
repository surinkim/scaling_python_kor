import socket

import fixtures
from pifpaf.drivers import memcached


class TestWithMemcached(fixtures.TestWithFixtures):
    def setUp(self):
        super(TestWithMemcached, self).setUp()
        self.memcached = self.useFixture(memcached.MemcachedDriver(port=9742))

    def test_connect(self):
        s = socket.socket()
        s.connect(("localhost", self.memcached.port))