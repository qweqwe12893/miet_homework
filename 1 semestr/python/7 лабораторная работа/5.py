# Дополните предыдущую задачу обработкой возможных исключений, связанных с
# сетевыми ошибками или неверными URL.
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
            if response.status == 200:
                 print(f'Подключение к {url} успешно (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')
            else:
                print(f'Не удалось получить данные от {url}. Статус: {response.status}')

    except aiohttp.ClientConnectionError:
        print(f'Произошла ошибка подключения при попытке получить данные  от {url}')
    except aiohttp.ClientTimeout:
        print(f'Время ожидания от {url} истекло')
    except aiohttp.ClientError as e:
        print(f'Упс... возникла ошибка клиента {url}: {e}')
    except Exception as e:
        print(f'Упс... возникла ошибка: {e}')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_status(session, url))

        # запускает и ждет завершения
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())