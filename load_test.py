import asyncio
import time
import httpx


async def make_request(client, user_id):

    start = time.time()

    response = await client.get(
        f"http://localhost:8000/recommendations/{user_id}"
    )

    elapsed = (time.time() - start) * 1000

    return elapsed


async def main():

    async with httpx.AsyncClient() as client:

        tasks = [
            make_request(client, (i % 10) + 1)
            for i in range(10)
        ]

        results = await asyncio.gather(*tasks)

        avg_time = sum(results) / len(results)

        print(f"Average Response Time: {avg_time:.2f}ms")


asyncio.run(main())