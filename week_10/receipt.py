# CSV reader Module.
import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# read_dictionary key_column_index:
PRODUCT_INDEX = 0

# request.csv indexes:
REQUEST_KEY_INDEX = 0
REQUEST_QUANTITY_INDEX = 1

# products_dict indexes:
REQUESTED_PRODUCT_NAME_INDEX = 1
REQUESTED_PRODUCT_PRICE_INDEX = 2

def main():
    """Function that call the read_dictionary function and  read_request function and print the receipt."""
    try:
        # try block.
        products_dict = read_dictionary("products.csv", PRODUCT_INDEX)
        number_of_items = 0
        subtotal = 0
        with open("request.csv", "rt") as request_csv_file:
            reader = csv.reader(request_csv_file)
            next(reader)
            print(f"Inkom Emporium\n")
            for requested_order_info in reader:
                requested_product_key = requested_order_info[REQUEST_KEY_INDEX]
                requested_product_quantity = float(requested_order_info[REQUEST_QUANTITY_INDEX])
                number_of_items += requested_product_quantity
                requested_product_name = None
                requested_product_price = None
                requested_product_info = products_dict[requested_product_key]
                requested_product_name = requested_product_info[REQUESTED_PRODUCT_NAME_INDEX]
                requested_product_price = float(requested_product_info[REQUESTED_PRODUCT_PRICE_INDEX])
                subtotal = subtotal + (requested_product_quantity * requested_product_price)
                print(f"{requested_product_name}: {requested_product_quantity} @ {requested_product_price}")

        # math operation. and stretch challenge
        print(f"\nNumber of Items: {number_of_items:.0f}")
        day_of_week = current_date_and_time.weekday()
        if day_of_week == 1:
            discount = subtotal * 0.1
            subtotal_with_discount = subtotal - discount
            sales_tax = subtotal * 0.06
            total = subtotal_with_discount + sales_tax
            print(F"Subtotal: {subtotal:.2f}\nTuesday special discount: {discount:.2f}\nSales Tax: {sales_tax:.2f}\nTotal: {total:.2f}")
        elif day_of_week == 2:
            discount = subtotal * 0.1
            subtotal_with_discount = subtotal - discount
            sales_tax = subtotal * 0.06
            total = subtotal_with_discount + sales_tax
            print(F"Subtotal: {subtotal:.2f}\nWednesday special discount: {discount:.2f}\nSales Tax: {sales_tax:.2f}\nTotal: {total:.2f}")
        else:
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax
            # f-string to print the math operation.
            print(f"Subtotal: {subtotal:.2f}\nSales Tax: {sales_tax:.2f}\nTotal: {total:.2f}")
        
        # f-string to print the current time.
        print(f"\nThank you for shopping at the Inkom Emporium.\n{current_date_and_time:%a %b %d %H:%M:%S %Y}")
        print(f"\nHave a moment?\nPlease take our online survey at wwww.inkomemporium.com/onlinesurvey.php") # challenge online survey invitation.
    
    # file nof found handler.
    except FileNotFoundError as not_file_found_err:
        # This code will be executed if the csv files are not found.
        print(f"\n", type(not_file_found_err).__name__, not_file_found_err, sep=": ")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the {request_csv_file.name} file {key_err}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file."""
    products_dict = {}
    with open(filename, "rt") as products_csv_file:
        reader = csv.reader(products_csv_file)
        next(reader)
        for data in reader:
            if len(data) !=0:
                key = data[key_column_index]
                products_dict[key] = data
    return products_dict

# Call main to start this program.
if __name__ == "__main__":
    main()
