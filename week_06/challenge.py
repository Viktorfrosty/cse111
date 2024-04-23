def main():
    print("This program is an implementation of the Nature Relatedness Scale.")
    user_selections()
    pass

def user_selections():
    value = 0
    print("Enter 1 (Strongly disagreed), 2, 3, 4 or 5 (Agree strongly)")
    selection_1 = int(input("My ideal vacation spot would be a remote, wilderness area.= "))
    selection_calculation(value, selection_1)
    selection_2 = int(input("I always think about how my actions affect the environment.= "))
    selection_calculation(value, selection_2)
    selection_3 = int(input("My connection to nature and the environment is a part of my spirituality.= "))
    selection_calculation(value, selection_3)
    selection_4 = int(input("I take notice of wildlife wherever I am.= "))
    selection_calculation(value, selection_4)
    selection_5 = int(input("My relationship to nature is an important part of who I am.= "))
    selection_calculation(value, selection_5)
    selection_6 = int(input("I feel very connected to all living things and the earth.= "))
    selection_calculation(value, selection_6)
    print(f"Your score is {value:.2f}.")

def selection_calculation(value, selection):
    if selection == "D":
        value = value + 1
    elif selection == "d":
        value = value + 2
    elif selection == "":
        value = value + 3
    elif selection == 4:
        value = value + 4
    elif selection == 5:
        value = value + 5
    return value

def total_value_calculation(value):
    """
    Scoring Information: NR-6 score is calculated by averaging all 6 items.
    """
    total = value / 6
    return total

main()