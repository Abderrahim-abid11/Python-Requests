import asyncio
import httpx
import time


async def res():
    urls = ["https://www.google.com","https://www.github.com","http://example.com"]
    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)
    print(results)

start = time.perf_counter()
asyncio.run(res())
end = time.perf_counter()

print(end-start)
