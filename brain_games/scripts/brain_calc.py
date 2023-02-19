import prompt
import operator
import random
from random import randint
import brain_games.move 

task = 'What is the result of the expression?'


def get_question(a, b, c):
    return (str(a) + ' ' + c + ' ' + str(b))

def get_result(a,b,c):
    return action[c](a, b)

config = []
for q in range(0, 3):
    a = randint(1, 99)
    b = randint(1, 99)

    action = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
        }   
    simbol = ['*', '-', '+']
    c = random.choice(simbol)

    question = get_question(a, b, c)
    result = get_result(a, b, c)

    config.append([question, result]) # [[q, r], [q, r], [q ,r]]

# config



brain_games.move.play(task, config)








