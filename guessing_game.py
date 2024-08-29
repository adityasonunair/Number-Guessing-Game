import random
# this function will use the randint to generate a random number
# from 1 to 100 (inclusive)
def generate_number():
    print("Welcome to Aditya's Number Guessing Game!")
    return random.randint(1, 100)

def compare(guessed_number, actual_number):
    if guessed_number > actual_number:
        result = 'Too high'
    elif guessed_number < actual_number:
        result = 'Too low'
    else:
        result = 'Bingo'
    return result

actual_number = generate_number()
# print(actual_number)
score = 100
guessed_number = ''
while guessed_number != actual_number:
    guessed_number = int(input("Enter your guess: "))
    score -= 1
    results = compare(guessed_number, actual_number)
    print(results)

