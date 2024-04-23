def main():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.\nThis program will show you ten statements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the statements by responding with one of these four letters:\n\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")
    user_decitions()

def user_decitions():
    value = 0
    selection_1 = input("I feel that I am a person of worth, at least on an equal plane with others.\nEnter D, d, a, or A: ")
    value = positive_statements_calculation(value, selection_1)
    selection_2 = input(": I feel that I have a number of good qualities.\nEnter D, d, a, or A: ")
    value = positive_statements_calculation(value, selection_2)
    selection_3 = input("All in all, I am inclined to feel that I am a failure.\nEnter D, d, a, or A: ")
    value = negative_statements_calculation(value, selection_3)
    selection_4 = input("I am able to do things as well as most other people.\nEnter D, d, a, or A: ")
    value = positive_statements_calculation(value, selection_4)
    selection_5 = input("I feel I do not have much to be proud of.\nEnter D, d, a, or A: ")
    value = negative_statements_calculation(value, selection_5)
    selection_6 = input("I take a positive attitude toward myself.\nEnter D, d, a, or A: ")
    value = positive_statements_calculation(value, selection_6)
    selection_7 = input("On the whole, I am satisfied with myself.\nEnter D, d, a, or A: ")
    value = positive_statements_calculation(value, selection_7)
    selection_8 = input("I wish I could have more respect for myself.\nEnter D, d, a, or A: ")
    value = negative_statements_calculation(value, selection_8)
    selection_9 = input("I certainly feel useless at times.\nEnter D, d, a, or A: ")
    value = negative_statements_calculation(value, selection_9)
    selection_10 = input("At times I think I am no good at all.\nEnter D, d, a, or A: ")
    value = negative_statements_calculation(value, selection_10)
    print(f"Your score is {value}.\nA score below 15 may indicate problematic low self-esteem.")

def positive_statements_calculation(value, selection):
    """
    The statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:
    Choice / Points
    Strongly Disagree / 0
    Disagree / 1
    Agree / 2
    Strongly Agree / 3
    """
    if selection == "D":
        value = value + 0
    elif selection == "d":
        value = value + 1
    elif selection == "a":
        value = value + 2
    elif selection == "A":
        value = value + 3
    return value

def negative_statements_calculation(value, selection):
    """
    The statements (numbers 3, 5, 8, 9, 10) are positive and are scored like this:
    Choice / Points
    Strongly Disagree / 3
    Disagree / 2
    Agree / 1
    Strongly Agree / 0
    """
    if selection == "D":
        value = value + 3
    elif selection == "d":
        value = value + 2
    elif selection == "a":
        value = value + 1
    elif selection == "A":
        value = value + 0
    return value

if __name__ == "__main__":
    main()