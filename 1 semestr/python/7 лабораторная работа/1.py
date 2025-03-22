# Напишите асинхронную функцию, которая читает содержимое файла и возвращает его в
# виде строки. Используйте библиотеку aiofiles.
import aiofiles
import asyncio


async def read_file(file_path):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
        
        # пока не прочитается содержимое
        # передает управление в main
        contents = await file.read()

    return contents


async def main():
    try:
        content = await read_file("t.txt")
        print(content)
    except FileNotFoundError:
        print("Не надо придумывать названия файлов. Введите существующее")


# точка входа
if __name__ == "__main__":
    asyncio.run(main())