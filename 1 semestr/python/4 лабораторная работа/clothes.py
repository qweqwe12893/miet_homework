from product import *

class Clothes(Product):
    def __init__(self, price, volume, color='black'):
        Product.__init__(self, price, volume) 
        self.__color = color
        
    def  __str__(self):
        return f"Clothes(price={self.price}, volume={self.volume}, color={self.__color})"

    def get_color(self):
        print(f"Этот товар имеет {self.__color } цвет")
        return self.__color
    
    def set_color(self, new):
        print(f"Цвет изменен на {new}")
        self.__color = new
