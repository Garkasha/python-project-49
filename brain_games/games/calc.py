import operator
import random
from random import randint
from brain_games.move import ask_questions_and_get_result


def task():
    print('What is the result of the expression?')


def make_task():
    a = randint(1, 99)
    b = randint(1, 99)

    action = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul}
    simbol = ['*', '-', '+']
    c = random.choice(simbol)

    question = (str(a) + ' ' + c + ' ' + str(b))
    result = action[c](a, b)
    return question, result


ask_questions_and_get_result(make_task, task)
