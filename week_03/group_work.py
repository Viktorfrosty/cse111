""" Work as a team to write a Python program named fitness.py that does the following:

Asks the user to enter four values:
gender
birthdate in this format: YYYY-MM-DD
weight in U.S. pounds
height in U.S. inches
Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
Converts inches to centimeters (1 in = 2.54 cm).
Calculates age, BMI, and BMR.
Prints age, weight in kg, height in cm, BMI, and BMR. """

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

"""core requirements"""
# def main():
#     # Get the user's gender, birthdate, height, and weight.
#     gender = input("Please enter your gender (M or F): ")
#     birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
#     inches = float(input("Enter your height in U.S. inches: "))
#     pounds = float(input("Enter your weight in U.S. pounds: "))
#     # Call the compute_age, kg_from_lb, cm_from_in,
#     # body_mass_index, and basal_metabolic_rate functions
#     # as needed.
#     years = compute_age(birth_str)
#     weight = kg_from_lb(pounds)
#     height = cm_from_in(inches)
#     bmi = body_mass_index(weight, height)
#     bmr = basal_metabolic_rate(gender, weight, height, years)
#     # Print the results for the user to see.
#     print(F"Age (years): {years}\nWeight (kg): {weight:.2f}\nHeight (cm): {height:.1f}\nBody mass index: {bmi:.1f}\nBasal metabolic rate (kcal/day): {bmr:.0f}")
#     pass

# def compute_age(birth_str):
#     """Compute and return a person's age in years.
#     Parameter birth_str: a person's birthdate stored
#         as a string in this format: YYYY-MM-DD
#     Return: a person's age in years.
#     """
#     # Convert a person's birthdate from a string
#     # to a date object.
#     birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
#     today = datetime.now()

#     # Compute the difference between today and the
#     # person's birthdate in years.
#     years = today.year - birthdate.year

#     # If necessary, subtract one from the difference.
#     if birthdate.month > today.month or \
#         (birthdate.month == today.month and \
#             birthdate.day > today.day):
#         years -= 1
#     return years

# def kg_from_lb(pounds):
#     """Convert a mass in pounds to kilograms.
#     Parameter pounds: a mass in U.S. pounds.
#     Return: the mass in kilograms.
#     """
#     weight = pounds * 0.45359237
#     return weight

# def cm_from_in(inches):
#     """Convert a length in inches to centimeters.
#     Parameter inches: a length in inches.
#     Return: the length in centimeters.
#     """
#     height = inches * 2.54
#     return height

# def body_mass_index(weight, height):
#     """Compute and return a person's body mass index.
#     Parameters
#         weight: a person's weight in kilograms.
#         height: a person's height in centimeters.
#     Return: a person's body mass index.
#     """
#     bmi = (10000 * weight)/(height**2)
#     return bmi

# def basal_metabolic_rate(gender, weight, height, age):
#     """Compute and return a person's basal metabolic rate.
#     Parameters
#         weight: a person's weight in kilograms.
#         height: a person's height in centimeters.
#         age: a person's age in years.
#     Return: a person's basal metabolic rate in kcals per day.
#     """
#     if gender == "M":
#         bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
#         return bmr
#     elif gender == "F":
#         bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
#         return bmr

"""Stretch Challenges"""
def main():
        gender = input("Please enter your gender (M or F): ")
        birth_str = input("Enter your birthdate (YYYY-MM-DD): ")  
        years = compute_age(birth_str)
        weight = get_weight()
        height = get_height()
        bmi = body_mass_index(weight, height)
        bmr = basal_metabolic_rate(gender, weight, height, years)
        print(F"Age (years): {years}\nWeight (kg): {weight:.2f}\nHeight (m): {(height/100):.2f}\nBody mass index: {bmi:.1f}\nBasal metabolic rate (kcal/day): {bmr:.0f}")

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years

def get_weight():
    user_weight_selection = input("enter the weight unit (kg or lb or st):")
    if user_weight_selection == "kg":
        weight = float(input("Enter your weight: "))
    elif user_weight_selection == "lb":
        pounds = float(input("Enter your weight: "))
        weight = kg_from_lb(pounds)
    elif user_weight_selection == "st":
        stones = float(input("Enter your weight: "))
        weight = kg_from_st(stones)
    return weight

def kg_from_lb(pounds):
    weight = pounds * 0.45359237
    return weight

def kg_from_st(stones):
    weight = stones * 6.35029318
    return weight

def get_height():
    user_height_selection = input("Enter the heigth unit (cm or ft or in)")
    if user_height_selection == "cm":
        height = float(input("Enter your height: "))
    elif user_height_selection == "ft":
        feets = float(input("Enter your height: "))
        height = cm_from_ft(feets)
    elif user_height_selection == "in":
        inches = float(input("Enter your height: "))
        height = cm_from_in(inches)
    return height

def cm_from_in(inches):
    height = inches * 2.54
    return height

def cm_from_ft(feets):
    height = feets * 30,48
    return height

def body_mass_index(weight, height):
    bmi = (10000 * weight)/(height**2)
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender == "M":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        return bmr
    elif gender == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
        return bmr

main()