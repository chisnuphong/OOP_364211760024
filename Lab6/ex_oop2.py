"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

class Student:
    #class attributes
    uni = "RUTS"
    my_std = [] # empty list

    def __init__(self,name,id,major):
        # object attributes
        self.name = name
        self.id = id
        self.major = major
        # add object to my_std (list)
        self.my_std.append(self)

    def introduce(self):
        print(f'My name is {self.name},'
              f' My id is {self.id} '
              f'and I am studying in {self.major} major.')

s1 = Student("chisnuphong channual","024","MIT")
s1.introduce()

s2 = Student("kheem","065","MT")
s2.introduce()

s1.major = "LM"
s1.introduce()

print(s1.uni)
print(s2.uni)

Student.uni = "PSU"
print(s1.uni)
print(s2.uni)

s1.uni = "WU"
print(s1.uni)
print(s2.uni)

print(len(Student.my_std))

print(Student.my_std[0].introduce())