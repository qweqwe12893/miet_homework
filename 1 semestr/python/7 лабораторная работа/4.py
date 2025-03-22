# Используйте библиотеку aiohttp для выполнения асинхронных HTTP-запросов.
# Напишите корутину, которая запрашивает данные с нескольких веб-сайтов (список и
# количество веб-сайтов выберите самостоятельно) и выводит статус ответа.

import aiohttp
import asyncio


urls = [
    'https://cat-bounce.com/',
    'https://non.existing.site',
    'http://www.staggeringbeauty.com/',
    'https://corgiorgy.com/'
]


async def fetch_status(session, url):
    try:
        async with session.get(url) as response:
            print(f'Статус-код для {url}: {response.status}')
    except Exception as e:
        print(f'Упс... не получилось достучаться до {url} (×_×)')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_status(session, url))

        # запускает и ждет завершения
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())