"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

class Labtop:

    def __init__(self,brand,model,cpu,ram,display,storage,price):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price


    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram

    def get_display(self):
        return self.__display
    def set_display(self,display):
        self.__display = display

    def get_storage(self):
        return self.__storage
    def set_storage(self,storage):
        self.__storage = storage

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def __str__(self):
        print(f'Brand: {self.__brand}, '
              f'Model: {self.__model}, '
              f'Cpu: {self.__cpu}, '
              f'Ram: {self.__ram}, '
              f'Display: {self.__display}, '
              f'Storage: {self.__storage}, '
              f'Price: {self.__price}')

l = Labtop("ASUS","Vivobook 15X","Intel Core",8,15.6,512,27900)
l.__str__()

print(l.get_brand())
l.set_brand("Acer")
print(l.get_brand())

print(l.get_price())
l.set_price(50000)
print(l.get_price())



