from random import randint
import brain_games.move

task = 'Answer "yes" if the nomber is even, otherwise answer "no".'

config = []

for q in range(0, 3):
    number = randint(1, 99)

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    if is_even(number) is True:
        result = 'yes'
    else:
        result = 'no'

    question = str(number)
    config.append([question, result])


def main():
    brain_games.move.play(task, config)


if __name__ == '__main__':
    main()
