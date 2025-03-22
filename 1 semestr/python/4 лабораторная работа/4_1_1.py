from product import *
from food import Food
from clothes import Clothes

        
print("\n\n==========Класс Product==========")

product1 = Product(price=100, volume=10)  # конструктор __init__
print(product1)                           # строковое представление объекта
product1.discount(60)                     # скидка на продукт в 60%
product1.capacity(20, 20, 20)             # кол-во товара, вместимого в контейнер объемом 800 единиц
print()

product2 = Product()                      # дефолтный для всех классов конструктор
product2.price = 15                       # изменение стандартного значения на свое
product2.volume = 10                      # изменение стандартного значения на свое
print(product2)                           # строковое представление объекта
product2.discount(30)                     # скидка на продукт в 30%
product2.capacity(13, 2, 3)               # кол-во товара, вместимого в контейнер объемом 78 единиц
print()

product3 = Product(1, 3)                  # конструктор __init__
print(product3)                           # строковое представление объекта
product3.discount(20)                     # скидка на продукт в 20%
product3.capacity(2, 3, 4)                # кол-во товара, вместимого в контейнер объемом 24 единиц
print("Увеличение цены: ")
print(15 + product3 + 2)                  # вывод объекта при увеличении цены на 17 руб
print()


print("\n\n==========Класс Food==========" )

cheese = Food(50, 30, 500)
print(cheese)                              # строковое представление объекта
cheese.discount(30)                        # скидка на продукт в 30%
print(12 + cheese)                         # прибавление калорий

ы
print("\n\n==========Класс Clothes==========" )

jeans = Clothes(3000, 200, 'серо-буро-малиновый')
print(jeans)
jeans.get_color()                          
jeans.set_color("скандальный оранжевый")
