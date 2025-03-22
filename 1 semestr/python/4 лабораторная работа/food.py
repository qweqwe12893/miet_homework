from product import *

class Food(Product):
    def __init__(self, price, volume, calories=100):
        super().__init__(price, volume)
        self.__calories = calories

    def  __str__(self):
        return f"Food(price={self.price}, volume={self.volume}, calories={self.__calories})"


    def __add__(self, other):
        print(f"Продукт при повышении калорий на {other}")
        return Food(self.price, self.volume, self.__calories + other)

    def __radd__(self, other):
        if (type(other) == int or type(other) == float):
            print(f"Продукт при повышении калорий на {other}")
            return Food(self.price, self.volume, self.__calories + other)
        else:
            print("Калории должны быть целым неотрицательным числом") 
            return 0
