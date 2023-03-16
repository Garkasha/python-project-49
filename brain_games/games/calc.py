import operator
import random
from random import randint


DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():

    a = randint(1, 99)
    b = randint(1, 99)

    action = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul}

    c = random.choice(list(action.keys()))

    question = f'{a} {c} {b}'
    result = str(action[c](a, b))

    return question, result
