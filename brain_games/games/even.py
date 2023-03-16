from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round_data():
    question = randint(1, 99)

    if is_even(question):
        result = 'yes'
    else:
        result = 'no'

    return question, result
