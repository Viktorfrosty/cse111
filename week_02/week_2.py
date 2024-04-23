from datetime import datetime

# Core Requirements
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
"""  day_of_week = 0 """
subtotal = float(input("Please enter the subtotal: "))
if day_of_week == 1 and subtotal >= 50 or day_of_week == 2 and subtotal >= 50:
   discount=subtotal*0.1
   subtotal-=discount
   print(f"Discount: {discount:.2f}")
sales_tax = subtotal * 0.06
subtotal += sales_tax
print(f"Sales Tax: {sales_tax:.2f}\nTotal: {subtotal:.2f}")

# Strech requirements
def discount_operation(total):
   if subtotal >= 50:
      discount = subtotal * 0.1
      subtotal_with_discount = subtotal - discount
      sales_tax = subtotal_with_discount * 0.06
      total = subtotal_with_discount + sales_tax
      print(F"Your discount is {discount:.2f}\nSales tax: {sales_tax:.2f}\nTotal: {total:.2f}")
   elif subtotal < 50:
      sales_tax = subtotal * 0.06
      total = subtotal + sales_tax
      print(F"You need at least {(50-subtotal):.2f} more to be elegible for the especial discount.\nSales tax: {sales_tax:.2f}\nTotal is: {total:.2f}")

price = -1
subtotal = 0
while price != 0:
   current_date_and_time = datetime.now()
   day_of_week = current_date_and_time.weekday()
   price = float(input("Please enter the price (enter 0 to finish): "))
   if price != 0:
      quantity = int(input("Please enter the quantity: "))
      subtotal += price * quantity
      if day_of_week == 1:
         print("Today is Tuesday. ", end='')
         discount_operation(subtotal)
         price = -1
         subtotal = 0
      elif day_of_week == 2:
         print("Today is wednesday. ", end='')
         discount_operation(subtotal)
         price = -1
         subtotal = 0
      else:
         print(F"Your total is: {subtotal:.2f}")
         price = -1
         subtotal = 0

# import math
# from datetime import datetime

# current_date_and_time = datetime.now()
# print(f"{current_date_and_time:%Y-%m-%d}")
# tire_width=float(input("Enter the width of the tire in mm (ex 205): "))
# tire_ratio=float(input("Enter the aspect ratio of the tire (ex 60): "))
# tire_diameter=float(input("Enter the diameter of the wheel in inches (ex 15): "))
# tire_volume=(math.pi*tire_width**2*tire_ratio*(tire_width*tire_ratio+2540*tire_diameter))/10000000000
# print(F"The approximate volume is {tire_volume:.2f} liters")
# with open("volumes.txt", "at") as tires_file:
#     print(F"{current_date_and_time}, {tire_width:.2f}, {tire_ratio:.2f}, {tire_diameter:.2f}, {tire_volume:.2f}", file = tires_file)