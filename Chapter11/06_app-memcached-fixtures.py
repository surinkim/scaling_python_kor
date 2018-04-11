import fixtures
from pifpaf.drivers import memcached
from pymemcache import client


class AppException(Exception):
    pass


class Application(object):
    def __init__(self, memcached=("localhost", 11211)):
        self.memcache = client.Client(memcached)

    def store_settings(self, settings):
        self.memcache.set("appsettings", settings)

    def retrieve_settings(self):
        return self.memcache.get("appsettings")


class TestWithMemcached(fixtures.TestWithFixtures):
    def test_store_and_retrieve_settings(self):
        self.memcached = self.useFixture(memcached.MemcachedDriver(port=9742))
        self.app = Application(("localhost", self.memcached.port))
        self.app.store_settings(b"foobar")
        self.assertEqual(b"foobar", self.app.retrieve_settings())