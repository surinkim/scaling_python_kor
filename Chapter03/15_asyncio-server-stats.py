import asyncio
import time

SERVER_ADDRESS = ('127.0.0.1', 1234)


class YellEchoServer(asyncio.Protocol):
    def __init__(self, stats):
        self.stats = stats
        self.stats['started at'] = time.time()

    def connection_made(self, transport):
        self.transport = transport
        self.stats['connections'] += 1

    def data_received(self, data):
        self.transport.write(data.upper())
        self.stats['messages sent'] += 1


event_loop = asyncio.get_event_loop()

stats = {
    "started at": time.time(),
    "connections": 0,
    "messages sent": 0,
}

factory = event_loop.create_server(
    lambda: YellEchoServer(stats), *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)

try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    event_loop.close()

    ran_for = time.time() - stats['started at']
    print("Server ran for: %.2f seconds" % ran_for)
    print("Connections: %d" % stats['connections'])
    print("Messages sent: %d" % stats['messages sent'])
    print("Messages sent per second: %.2f"
        % (stats['messages sent'] / ran_for))