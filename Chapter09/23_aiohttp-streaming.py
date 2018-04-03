import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.content.read()

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(get("http://example.com"))]
loop.run_until_complete(asyncio.wait(tasks))
print("Results: %s" % [task.result() for task in tasks])