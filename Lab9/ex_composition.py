"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

# Class Relations - Composition

class Faculty:
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Faculty name: {self.fac_name}')

class University:
    lst_faculty = list()
    def __init__(self,uniname):
        self.uniname = uniname
        self.get_faclty()
    def uni_info(self):
        print(f'University name: {self.uniname}')
        print(f'has faculty bolow: ')
        if len(self.lst_faculty) ==0:
            print(f'Has no faculty.')
        else:
            for x in self.lst_faculty:
                x.fac_info()

    def get_faclty(self):
        f1 = Faculty("MT")
        f2 = Faculty("Sci-Tech")
        self.lst_faculty.append(f1)
        self.lst_faculty.append(f2)

u1 = University("RUTS")

u1.uni_info()

u1.lst_faculty[0].fac_info()
