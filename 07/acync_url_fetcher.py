import argparse
import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(concurrency, url_file):
    async with aiohttp.ClientSession() as session:
        tasks = []
        with open(url_file, 'r', encoding='utf-8') as file:
            urls = file.read().splitlines()

        semaphore = asyncio.Semaphore(concurrency)

        async def fetch_url_with_semaphore(url):
            async with semaphore:
                response = await fetch_url(session, url)
                print(f'URL: {url}\nResponse: {response}\n')

        for url in urls:
            task = fetch_url_with_semaphore(url)
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Async URL fetcher')
    parser.add_argument('concurrency', type=int, help='Number of concurrent requests')
    parser.add_argument('url_file', type=str, help='File containing the list of URLs')
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.concurrency, args.url_file))
