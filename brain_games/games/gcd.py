from random import randint
from brain_games.move import ask_questions_and_get_result


def task():
    print('Find the greatest common divisor of given numbers.')


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
    question = (str(a) + ' ' + str(b))
    result = find_hcf(a, b)

    return question, result


ask_questions_and_get_result(make_task, task)
