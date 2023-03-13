from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_hcf(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def make_task():
    a = randint(1, 99)
    b = randint(1, 99)
    question = f'{a} {b}'
    result = str(find_hcf(a, b))

    return question, result
