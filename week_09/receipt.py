import csv

# read_dictionary key_column_index:
PRODUCT_INDEX = 0

# request.csv indexes:
REQUEST_KEY_INDEX = 0
REQUEST_QUANTITY_INDEX = 1

# products_dict indexes:
REQUESTED_PRODUCT_NAME_INDEX = 1
REQUESTED_PRODUCT_PRICE_INDEX = 2

def main():
    """Function that call the read_dictionary function, read the request.csv file and print the requested product information."""
    products_dict = read_dictionary("week_09\products.csv", PRODUCT_INDEX) # change the filename path before submit!
    print("All products:")
    print(products_dict)
    print(f"\nRequested Items:")
    with open("week_09\_request.csv", "rt") as request_csv_file: # change the filename path before submit!
        reader = csv.reader(request_csv_file)
        next(reader)
        for requested_order_info in reader:
            requested_product_key = requested_order_info[REQUEST_KEY_INDEX]
            requested_product_quantity = requested_order_info[REQUEST_QUANTITY_INDEX]
            requested_product_name = ""
            requested_product_price = 0.00
            if requested_product_key in products_dict:
                requested_product_info = products_dict[requested_product_key]
                requested_product_name = requested_product_info[REQUESTED_PRODUCT_NAME_INDEX]
                requested_product_price = requested_product_info[REQUESTED_PRODUCT_PRICE_INDEX]
            print(f"{requested_product_name}: {requested_product_quantity} @ {requested_product_price}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
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