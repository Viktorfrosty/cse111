import math
item_value = int(input("Enter the number of items: "))
item_in_box = int(input("Enter the number of items per box :"))
box_needed = item_value/item_in_box
print(F"For {item_value} items, packing {item_in_box} items in each box, you will need {math.ceil(box_needed)} boxes.")
#   print(F"For {item_value} items, packing {item_in_box} items in each box, you will need {box_needed:.0f} boxes.")