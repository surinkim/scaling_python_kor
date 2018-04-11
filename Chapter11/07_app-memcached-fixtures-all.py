import fixtures
from pifpaf.drivers import memcached
from pymemcache import client
from pymemcache import exceptions


class AppException(Exception):
    pass


class Application(object):
    def __init__(self, memcached=("localhost", 11211)):
        self.memcache = client.Client(memcached)

    def store_settings(self, settings):
        try:
            self.memcache.set("appsettings", settings)
        except (exceptions.MemcacheError,
               ConnectionRefusedError,
               ConnectionResetError):
            raise AppException

def retrieve_settings(self):
    try:
        return self.memcache.get("appsettings")
    except (exceptions.MemcacheError,
           ConnectionRefusedError,
           ConnectionResetError):
        raise AppException


class TestWithMemcached(fixtures.TestWithFixtures):
    def test_store_and_retrieve_settings(self):
        self.memcached = self.useFixture(memcached.MemcachedDriver(port=9742))
        self.app = Application(("localhost", self.memcached.port))
        self.app.store_settings(b"foobar")
        self.assertEqual(b"foobar", self.app.retrieve_settings())

    def test_connect_fail_on_store(self):
        self.app = Application(("localhost", 123))
        self.assertRaises(AppException,
                        self.app.store_settings,
                        b"foobar")

    def test_connect_fail_on_retrieve(self):
        self.memcached = memcached.MemcachedDriver(port=9743)
        self.memcached.setUp()
        self.app = Application(("localhost", self.memcached.port))
        self.app.store_settings(b"foobar")
        self.memcached.cleanUp()
        self.assertRaises(AppException, 
                        self.app.retrieve_settings)

    def test_memcached_restarted(self):
        self.memcached = memcached.MemcachedDriver(port=9744)
        self.memcached.setUp()
        self.app = Application(("localhost", self.memcached.port))
        self.app.store_settings(b"foobar")
        self.memcached.reset()
        self.addCleanup(self.memcached.cleanUp)
        self.assertRaises(AppException, 
                        self.app.retrieve_settings)