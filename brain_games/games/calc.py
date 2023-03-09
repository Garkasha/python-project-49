import operator
import random
from random import randint


DESCRIPTION = 'What is the result of the expression?'


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
