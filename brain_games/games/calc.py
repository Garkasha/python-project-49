import operator
import random
from random import randint
import brain_games.move


task = 'What is the result of the expression?'

config = []


for q in range(0, 3):
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

    config.append([question, result])  # [[q, r], [q, r], [q ,r]]


def main():
    brain_games.move.play(task, config)


if __name__ == '__main__':
    main()
