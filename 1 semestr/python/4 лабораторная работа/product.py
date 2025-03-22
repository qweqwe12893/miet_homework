class Product:
    def __init__(self, price = 0, volume = 0):

        if type(price) != int and type(price) != float or price < 0:
            print("Цена должна быть неотрицательным числом")
        else:
            self.price = price
            
        if type(volume) != int and type(volume) != float or volume < 0:
            print("Объем должен быть неотрицательным числом")
        else:
            self.volume = volume


    def  __str__(self):
        return f"Product(price={self.price}, volume={self.volume})"
    
    def discount(self, percent):
        res = round(self.price - self.price * percent / 100, 2)
        print(f"Цена товара со скидкой {percent}% равна {res} руб")
        return res


    def capacity(self, x, y, z):
        V = x * y * z
        amount = V // self.volume
        print(f"В контейнер объемом {V} ед. может вместиться {amount} шт товаров, каждый объемом в {self.volume} ед.")
        return amount

    def __add__(self, other):
        return Product(self.price + other, self.volume)

    def __radd__(self, other):
        if (type(other) == int or type(other) == float):
            return Product(self.price + other, self.volume)
        else:
            print(type(self)) 
            return 0

