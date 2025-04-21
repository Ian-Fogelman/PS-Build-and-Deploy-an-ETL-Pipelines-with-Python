import aiohttp
import asyncio
import time

async def fetch_data(session, url):
    async with session.get(url) as r:
        if r.status == 200:
            data = await r.json()
            #print(data) #Optional: uncomment to see response data
        else:
            print("Error:", r.status)

async def main():
    num_iterations = 2000
    url = "http://127.0.0.1:5000/random-user"  # API Endpoint
    print('Executing REST API call in async.py to {url} for {num_iterations} iterations.'.format(url=url,num_iterations=num_iterations))
    start_time = time.time()  # Start time

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for _ in range(2000)]
        await asyncio.gather(*tasks)  # Run all requests concurrently

    end_time = time.time()  # End time
    print(f"Total Execution Time for async.py: {end_time - start_time:.2f} seconds")

# Run the async function
asyncio.run(main())
