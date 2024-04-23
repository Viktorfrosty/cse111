"Core Requirements"
# from datetime import datetime

# current_date_and_time = datetime.now()
# day_of_week = current_date_and_time.weekday()
# # day_of_week = 0
# subtotal = float(input("Please enter the subtotal: "))
# if day_of_week == 1 and subtotal >= 50 or day_of_week == 2 and subtotal >= 50:
#    discount=subtotal*0.1
#    subtotal-=discount
#    print(f"Discount: {discount:.2f}")
# sales_tax = subtotal * 0.06
# subtotal += sales_tax
# print(f"Sales Tax: {sales_tax:.2f}\nTotal: {subtotal:.2f}")

"Strech requirements"
from datetime import datetime

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