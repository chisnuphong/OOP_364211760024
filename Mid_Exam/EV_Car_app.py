"""
Name: {chisnuphong channual}
SID: {364211760024}
Group: {MIT221}
"""
from EV_Car import EV_Car

# display
def display_evcar():
    if len(my_evcar) ==0:
        print("You had no evcar data.")
    else:
        print(f'You had {len(my_evcar)} following:')
        for x in my_evcar:
            x.evcar_detail()
        print("\n")


# option
def display_option_system():
    print("Welcome to EV_Car Data Store System ")
    print("1.Add EV_Car")
    print("2.Display all EV_Car")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_evcar_data()
    elif select==2:
        display_evcar()
    elif select ==3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")


# input data
def input_evcar_data():
    no = input("Enter evcar no:")
    brand = input("Enter evcar brand:")
    model = input("Enter evcar model:")
    motor = input("Enter evcar motor:")
    horsepower = int(input("Enter evcar horse power:"))
    batterysize = float(input("Enter evcar battery size:"))
    range = int(input("Enter evcar range: "))
    price = int(input("Enter evcar price: "))


    my_evcar.append(EV_Car(no,brand,model,motor,horsepower,batterysize,range,price))
    print("\n-----------------------------------")
    print("Already add vehicle to store.")
    print("\n-----------------------------------")



my_evcar = []
s = 0
while s == 0:
    display_option_system()