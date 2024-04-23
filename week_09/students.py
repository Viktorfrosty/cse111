import csv

def main():
    key_column_index = 0
    students_dict = read_dictionary("week_09\students.csv", key_column_index)
    student_id = input("Please enter an I-Number (xxxxxxxxx): ")
    id_lenght = len(student_id)
    if id_lenght == 9:
        if student_id in students_dict:
            student_info = students_dict[student_id]
            student_name = student_info[1] 
            print(student_name)
        else:
            print("Invalid I-Number")
    elif id_lenght < 9:
        print("Invalid I-Number: too few digits")
    elif id_lenght > 9:
        print("Invalid I-Number: too many digits")

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
    students_list = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for data in reader:
            if len(data) !=0:
                key = data[key_column_index]
                students_list[key] = data
    return students_list

if __name__ == "__main__":
    main()