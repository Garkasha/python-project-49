from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):

    if number == 0 or number == 1:
        return False

    n = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            n = n + 1
    if (n <= 0):
        return True


def make_task():

    question = randint(2, 99)

    if is_prime(question) is True:
        result = 'yes'
    else:
        result = 'no'

    return question, result
