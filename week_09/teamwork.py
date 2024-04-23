import csv
 
def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    students_dict = read_dictionary("week_09\students.csv", I_NUMBER_INDEX)
    inumber = input("Please enter an I-Number (xxxxxxxxx) or (xxx-xxx-xxx):")
    key_length = len(inumber)
    inumber = inumber.replace("-","")
    key_is_digit = inumber.isdigit()
    if key_is_digit == True:
        if key_length == 9:
            if inumber not in students_dict:
                print("No such student")
            else:
                value = students_dict[inumber]
                name = value[NAME_INDEX]
                print(name)
        elif key_length < 9:
            print("Invalid I-Number: too few digits")
        elif key_length > 9:
            print("Invalid I-Number: too many digits")
    else:
        print("Invalid I-Number")

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
    main()