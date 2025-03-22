# Создайте корутину, которая будет принимать имя и выводить приветствие через 2
# секунды. Создайте список имен и с помощью asyncio.gather() выполните корутину для
# каждого имени одновременно.

import asyncio


async def greet(name):
    await asyncio.sleep(2)  # ждем 2 сек
    print(f"Привет, {name}!")


async def main(names):

    # запускает несколькоо асинх задач и ждет их завершения
    await asyncio.gather(*(greet(name) for name in names))


names_list = ["Тролебузина",  # сочетание фамилий четырех вождей - Троцкого, Ленина, Бухарина и Зиновьева.
              "Даздраперма",  # Да здравствует Первое Мая!"
              "Даздрасмыгда", # Да здравствует смычка города и деревни.
              "Дональд"
             ]


if __name__ == "__main__":
    asyncio.run(main(names_list))