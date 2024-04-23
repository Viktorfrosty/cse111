import math
tire_width=float(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio=float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter=float(input("Enter the diameter of the wheel in inches (ex 15): "))
tire_volume=(math.pi*tire_width**2*tire_ratio*(tire_width*tire_ratio+2540*tire_diameter))/10000000000
print(F"The approximate volume is {tire_volume:.2f} liters")