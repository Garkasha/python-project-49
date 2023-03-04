import operator
import random
from random import randint


def make_task():

    task = 'What is the result of the expression?'
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

    return question, result, task
