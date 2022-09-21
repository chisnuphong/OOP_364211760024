"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

class Student:
    def __init__(self,name,id):
        # attributes
        self.__name = name  # public  member
        self.__id = id   # private  member
    # getter and setter
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__id

    def __str__(self):
        print(f'Name: {self.__name} ID: {self.__id}')


s = Student("Kheem","024")
s.__str__()

print(s.get_name())
s.set_name("Tee")

print(s.get_name())

print(s.get_id())