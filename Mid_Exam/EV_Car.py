"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""
class EV_Car:

    my_evcar = []

    def __init__(self,no,brand,model,motor,horsepower,batterysize,range,price):
        self.no = no
        self.brand = brand
        self.model = model
        self.motor = motor
        self.horsepower = horsepower
        self.batterysize = batterysize
        self.range = range
        self.price = price
        self.my_evcar.append(self)

    def evcar_detail(self):
        print(f'No:{self.no} '
              f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Motor:{self.motor} '
              f'Horse Power:{self.horsepower} '
              f'Battery Size:{self.batterysize} '
              f'Range:{self.range} '
              f'Price:{self.price}')

