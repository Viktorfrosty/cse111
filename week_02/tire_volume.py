import math
from datetime import datetime

current_date_and_time = datetime.now()
print(f"----------------------------------------------------------------------------------------------------------------------------------\nWelcome to the tire database program. (Alpha Build 0.02)\nCurrent date: {current_date_and_time:%Y-%m-%d}\n")
while True:
    print("\nPlease select one of the following options:\n1: register a tire.\n2: Print tire database.\n3: Close the program.\n")
    try:
        user_selection = int(input("Option number: "))
        if user_selection == 1:
            tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
            tire_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
            tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
            tire_volume=(math.pi*tire_width**2*tire_ratio*(tire_width*tire_ratio+2540*tire_diameter))/10000000000
            print(F"The approximate volume is {tire_volume:.2f} liters")
            tire_condition = input("Enter the condition of the tire: ")
            tire_id = input("Enter the id code of the tire: ")
            print("Tire added to the database.")
            with open("volumes.txt", "at") as tires_file:
                print(F"{current_date_and_time:%Y-%m-%d}, {tire_id}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f}, {tire_condition}", file = tires_file)
        elif user_selection == 2:
            with open("volumes.txt", "rt") as tire_database:
                print("\n[date / tire id code / tire width / tire ratio / tire diameter / tire condition]")
                for tire_especification in tire_database:
                    print(tire_especification, end='')
        elif user_selection == 3:
            print("Goodbye\n------------------------------------------------------------------------------------------")
            break
    except ValueError:
        print("Input a valid element.\n")