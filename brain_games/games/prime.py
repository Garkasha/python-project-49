from random import randint
import math

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if (number % i == 0):
            return False
    return True


def generate_round_data():

    question = randint(0, 99)

    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'

    return question, result
