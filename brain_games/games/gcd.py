from random import randint


def find_hcf(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def make_task():
    task = 'Find the greatest common divisor of given numbers.'
    a = randint(1, 99)
    b = randint(1, 99)
    question = (str(a) + ' ' + str(b))
    result = find_hcf(a, b)

    return question, result, task
