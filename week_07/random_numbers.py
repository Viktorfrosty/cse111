import random

"""Core Requirements:"""
# def main():
#     numbers_list = [16.2, 75.1, 52.3]
#     print(numbers_list)
#     append_random_numbers(numbers_list)
#     print(numbers_list)
#     append_random_numbers(numbers_list, 3)
#     print(numbers_list)

def append_random_numbers(numbers_list, quantity = 1): 
    while quantity != 0:
        random_number = f"{random.uniform(0.0,100.0):.1f}"
        numbers_list.append(float(random_number))
        quantity -= 1
    return numbers_list
"""Stretch Challenges:"""
def main():
    numbers_list = [16.2, 75.1, 52.3]
    words_list = []
    print(numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)
    append_random_words(words_list, 4)
    print(words_list)

def append_random_words(words_list, quantity = 1):
    while quantity != 0:
        random_word_list = ["Rabbit", "Dog", "Tomatoes", "Onion", "Mordor", "Decepticons", "Mom"]
        random_word = random.choice(random_word_list)
        words_list.append(random_word)
        quantity -= 1
    return words_list

if __name__ == "__main__":
    main()