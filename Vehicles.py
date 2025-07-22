import time
import os
class Vehicle:
    def __init__(self,regno,brand,price):
        self.regno=regno
        self.brand=brand
        self.price=price
    def display_info(self):
        pass
    def add_vehicle(self):
        pass

class car(Vehicle):
    def __init__(self, regno, brand, price,fueltype):
        super().__init__(regno, brand, price)
        self.fueltype=fueltype
    
    def display_info(self):
        print(f"|Reg#: {self.regno}| |Brand: {self.brand}| |Price: {self.price}| |Fuel Type: {self.fueltype}|")
    
    def add_vehicle(self):
        record = f"{self.regno},{self.brand},{self.price},{self.fueltype}\n"
        with open("car.txt", "a") as f:
            f.write(record)
        print("Car added successfully!")
        time.sleep(1.5)
        os.system('cls')
 
class bike(Vehicle):
    def __init__(self, regno, brand, price,fueltype):
        super().__init__(regno, brand, price)
        self.fueltype=fueltype
    
    def display_info(self):
        print(f"|Reg#: {self.regno}| |Brand: {self.brand}| |Price: {self.price}| |Fuel Type: {self.fueltype}|")
    
    def add_vehicle(self):
        record = f"{self.regno},{self.brand},{self.price},{self.fueltype}\n"
        with open("bike.txt", "a") as f:
            f.write(record)
        print("Bike added successfully!")
        time.sleep(1.5)
        os.system('cls')

def main_menu():
    while True:
        print("==============================================================")
        print(">>>>>>>>>>>>Welcome to Vehicles Mangement System<<<<<<<<<<<<<<")
        print("==============================================================")
        print("            1. Add vehicle                                    ")
        print("            2. Show all vehicle                               ")
        print("            3. Search by RegNo.                               ")
        print("            4. Exit                                           ")
        print("==============================================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            os.system('cls')
            print("Select the Type of Vehicle: ")
            print("1. Car\n2. Bike")
            type1 = int(input("Enter your Type: "))

            if type1 == 1:
                os.system('cls')
                num = input("Enter the Number of Car: ")
                with open("car.txt") as f:
                    f.seek(0)
                    content=f.read()
                    if num in content:
                        print("Car with this number already added!")
                        time.sleep(1)
                        os.system('cls')
                        main_menu()
                    else:
                        brand = input("Enter the Brand of Car: ")
                        price = input("Enter the Price of Car: ")
                        fueltype = input("Enter fuel Type: ")
                        new_car = car(num, brand, price, fueltype)
                        new_car.add_vehicle()
            elif type1==2:
                os.system('cls')
                num = input("Enter the Number of Bike: ")
                with open("bike.txt") as f:
                    f.seek(0)
                    content=f.read()
                    if num in content:
                        print("Bike with this number already added!")
                        time.sleep(1)
                        os.system('cls')
                        main_menu()
                    else:
                        brand = input("Enter the Brand of Bike: ")
                        price = input("Enter the Price of Bike: ")
                        fueltype = input("Enter fuel Type: ")
                        new_bike = bike(num, brand, price, fueltype)
                        new_bike.add_vehicle()
        elif choice==2:
            print("What U want to see......?")
            print("1. Car\n2. Bike")
            type2=int(input("Enter your choice: "))
            
            if type2 == 1:
                print("=" * 45)
                print(">>>>>>>>>Showing car record<<<<<<<<<")
                print("=" * 45)
                try:
                    with open("car.txt", "r") as f:
                        for line in f:
                            parts = line.strip().split(",")
                            if len(parts) >= 4:
                                regno = parts[0]
                                brand = parts[1]
                                price = parts[2]
                                fueltype = ",".join(parts[3:]) 
                                car_obj = car(regno, brand, price, fueltype)
                                car_obj.display_info() 
                except FileNotFoundError:
                    print("Car file not found.")
                input("\nPress Enter to go back to main menu...")
                main_menu()
            elif type2==2:
                print("=" * 45)
                print(">>>>>>>>>Showing car record<<<<<<<<<")
                print("=" * 45)
                try:
                    with open("bike.txt", "r") as f:
                        for line in f:
                            parts = line.strip().split(",")
                            if len(parts) >= 4:
                                regno = parts[0]
                                brand = parts[1]
                                price = parts[2]
                                fueltype = ",".join(parts[3:]) 
                                bike_obj = bike(regno, brand, price, fueltype)
                                bike_obj.display_info() 
                except FileNotFoundError:
                    print("Bike file not found.")
                input("\nPress Enter to go back to main menu...")
                main_menu()
        elif choice == 4:
            print("Exiting Program...")
            break
main_menu()