import argparse
import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(concurrency, url_file):
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(concurrency)

        async def fetch_url_with_semaphore(url):
            async with semaphore:
                response = await fetch_url(session, url)
                print(f'URL: {url}\nResponse: {response}\n')

        async def process_urls(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                while True:
                    chunk = await asyncio.to_thread(file.readlines, 100)  # Чтение файла построчно
                    if not chunk:
                        break

                    tasks = [fetch_url_with_semaphore(url.strip()) for url in chunk]
                    await asyncio.gather(*tasks)

        await process_urls(url_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Async URL fetcher')
    parser.add_argument('concurrency', type=int, help='Number of concurrent requests')
    parser.add_argument('url_file', type=str, help='File containing the list of URLs')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.concurrency, args.url_file))
