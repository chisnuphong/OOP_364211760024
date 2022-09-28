"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""

from Laptop import Labtop

# display
def display_laptop():
    if len(my_labtop) ==0:
        print("\nYou had no laptop data.\n")
    else:
        num = 1
        print(f'You had {len(my_labtop)} following')
    for x in my_labtop:
        print(f'{num}.',end="")
        x.display_labtop()
        num +=1
    print("\n")

# option
def display_option_system():
    print("Welcome to Laptop Data Store System")
    print("1.Add Labtop")
    print("2.Display all Labtop")
    print("3.Delete Labtop")
    print("4.Edit Labtop Price")
    print("5.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_laptop()
    elif select == 3:
        delete_laptop()
    elif select == 4:
        edit_laptop_price()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

def edit_laptop_price():
    print("Which one do you want to edit price?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n})or type 0 to main options:? "))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_price()}')
            newprice = float(input("enter new price:"))
            my_labtop[s-1].set_price(newprice)
            print("\nAlready delete laptop data.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")


# delete data
def delete_laptop():
    print("Which one do you want to remove?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n})or type 0 to main options:? "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete laptop data.\n")
            break
        elif s ==0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")

# input data
def input_laptop_data():
    brand = input("Enter laptop brand : ")
    model = input("Enter laptop model : ")
    cpu = input("Enter laptop CPU : ")
    ram = int(input("Enter laptop RAM(GB) : "))
    display = float(input("Enter laptop display(inch) : "))
    storage = int(input("Enter laptop storage(GB) : "))
    price = float(input("Enter laptop price : "))

    l = Labtop("","","",0,0,0,0)


    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)

    # my_labtop.append(Labtop(brand, model, cpu, ram, display, storage, price))
    my_labtop.append(l)
    print("\n------------------------------------")
    print("Already add laptop to store.")
    print("--------------------------------------")

my_labtop = []
my_labtop.append(Labtop("ASUS","Vivobook 15X","Intel Core i5-12500H",8,15.6,512,27900))
my_labtop.append(Labtop("Lenovo","IdeaPadGaming3","Intel Core i5-11320H",8,15.6,512,25990))
my_labtop.append(Labtop("Acer","Swift3","Intel Core i7-1260P",8,14,512,33990))
s = 0
while s == 0:
    display_option_system()