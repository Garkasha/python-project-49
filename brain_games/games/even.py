from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def make_task():
    question = randint(1, 99)

    if is_even(question) is True:
        result = 'yes'
    else:
        result = 'no'

    return question, result
