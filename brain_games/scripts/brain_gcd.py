#!/usr/bin/env python3
from random import randint
import brain_games.move

task = 'Find the greatest common divisor of given numbers.'


def find_hcf(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


config = []
for q in range(0, 3):
    a = randint(1, 99)
    b = randint(1, 99)
    question = (str(a) + ' ' + str(b))
    result = find_hcf(a, b)

    config.append([question, result])  # [[q, r], [q, r], [q ,r]]


def main():
    brain_games.move.play(task, config)


if __name__ == '__main__':
    main()
