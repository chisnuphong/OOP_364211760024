"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""
class Vihecle:
    #class attributes
    my_Vihecle = []

    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price
        self.my_Vihecle.append(self)

    def vihecle_detail(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Color:{self.color} '
              f'Max speed:{self.maxspeed} '
              f'Price:{self.price}')
