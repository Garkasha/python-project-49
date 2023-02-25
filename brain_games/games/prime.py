from random import randint
import brain_games.move

task = 'Answer \"yes\" if the nomber is prime, otherwise answer \"no\".'

config = []

for q in range(0, 3):
    number = randint(2, 99)

    def is_prime(number):
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True

    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'

    question = str(number)
    config.append([question, result])


def main():
    brain_games.move.play(task, config)


if __name__ == '__main__':
    main()
