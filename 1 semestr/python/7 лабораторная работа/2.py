# Напишите асинхронную функцию, которая выполняет обработку данных (задачу
# обработки данных придумайте самостоятельно). Используйте библиотеку asyncio.

import aiohttp
import asyncio


# GET-запрос для получения html-кода страницы
async def aiohttp_fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await aiohttp_fetch(session, 'http://endless.horse/')
        print(html)


if __name__ == "__main__":
    asyncio.run(main())