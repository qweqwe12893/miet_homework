
class PositiveInt(Exception):
    pass

def positive_int(a, name):
    if type(a) not in [int, float]:
        raise PositiveInt(f"упс... переменная {name} должна быть числового типа")
    elif a < 0:
        raise PositiveInt(f"упс... переменная {name} должна быть неотрицательным числом")
    return a



class Product:
    def __init__(self, price = 0, volume = 0):

        try:
            self.price = positive_int(price, 'price')
        except PositiveInt as e:
            print(f"Сообщение об ошибке: {e}")
            self.price=0

        try:
            self.volume = positive_int(volume, 'volume')
        except PositiveInt as e:
            print(f"Сообщение об ошибке: {e}")
            self.volume=0


    def  __str__(self):
        return f"Product(price={self.price}, volume={self.volume})"
    
    def discount(self, percent):
        try:
            percent = positive_int(percent, 'percent')
            res = round(self.price - self.price * percent / 100, 2)
            print(f"Цена товара со скидкой {percent}% равна {res} руб")
            return res
        except PositiveInt as e:
            print(f"Сообщение об ошибке: {e}")



    def capacity(self, x, y, z):
        V = x * y * z

        try:
            V = positive_int(V, 'отвечающая за объем')
            amount = V // self.volume
            print(f"В контейнер объемом {V} ед. может вместиться {amount} шт товаров, каждый объемом в {self.volume} ед.")
            return amount

        except PositiveInt as e:
            print(f"Сообщение об ошибке: {e}")



    def __add__(self, other):
        return Product(self.price + other, self.volume)

    def __radd__(self, other):
        try:
            return Product(self.price + other, self.volume)
        except:
            print("Ошибка: можно складывать только объект класса \
                  Product с объектом числового типа данных.")


    @staticmethod
    def read_from_file(filename):
        try:
            with open(filename, encoding='utf-8') as f:
                res = []
                for i in f.readlines():
                    res.append(i.strip())
                return res
        except FileNotFoundError:
            print("Ошибка: файл не найден. Проверьте правильность названия")

    @staticmethod
    def write_to_file(filename, line):
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(line+'\n')

        except TypeError:
            print(f"Ошибка: предоставлены некорректные данные для записи в файл")



readed = Product.read_from_file('from.txt')
#print(readed)

Product.write_to_file('to.txt', 'qwerqwr')
