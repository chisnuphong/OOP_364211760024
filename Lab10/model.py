"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

class Person:
    def __init__(self,name,age,weight,height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    def __str__(self):
        print(f'Name: {self.__name} '
              f'Age: {self.__age} '
              f'Weight: {self.__weight} '
              f'Height: {self.__height}')
        # getter and setter
        def get_name(self):
            return self.__name
        def set_name(self,name):
            self.__name = name
        def get_age(self):
            return self.__age
        def get_age(self,age):
            self.__age = age
        def set_weight(self):
            return self.__weight
        def get_weight(self,weight):
            self.__weight = weight
        def set_height(self):
             return self.__height
        def get_height(self, height):
            self.__height = height

class Student(Person):
    def __init__(self,name,age,weight,height,major):
        super().__init__(name,age,weight,height)
        self.__major = major
    def __str__(self):
        super().__str__()
        print(f'Major: {self.__major}')

class Vaccine:
    all_vaccine = ["Sinovac","Astrazeneca","Moderna","Pfizer","Sinopharm"]

    def __init__(self,vac_name):
        self.__vac_name = vac_name
    def vaccine_info(self):
        print(f'vaccine name: {self.__vac_name}')
    def get_name(self):
        return self.__vac_name
    def get_all_vaccine(self):
        for x in self.all_vaccine:
            print(x)

class Vaccine_Passport():
    def __init__(self,owner):
        self.owner = owner
        self.vaccinated = list()
        self.date = list()
    def add_vaccine(self,Vaccine):
        self.vaccinated.append(Vaccine)
    def add_date(self,date):
        self.date.append(date)
    def vaccine_passport_info(self):
        print(f'MT Vaccinated Passport: ')
        self.owner.__str__()
        c = 1
        if len(self.vaccinated) ==0:
            print(f'\tNo vaccinated date.')
        else:
            for x in range(len(self.vaccinated)):
                print(f'{c}. {self.vaccinated[x].get_name()}'
                      f' date: {self.date[x]}')
                c +=1











