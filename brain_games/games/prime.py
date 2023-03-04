from random import randint


def make_task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = randint(2, 99)

    def is_prime(number):
        n = 0
        for i in range(2, number // 2 + 1):
            if (number % i == 0):
                n = n + 1
        if (n <= 0):
            return True

    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'

    question = number

    return question, result, task
