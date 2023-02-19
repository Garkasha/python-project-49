import prompt
from random import randint


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')


def brain_even():
    print('Answer \"yes\" if the nomber is even, otherwise answer \"no\".')
    counter = 0
    while counter < 3:
        n = randint(1, 99)
        print('Question: ' + str(n))
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and n % 2 == 0) or (answer == 'no' and n % 2 == 1):
            print('Correct!')
            counter += 1
        else:
            if n % 2 == 0:
                print('\'' + answer + '\'' + ' is wrong answer ;(. Correct answer was \'yes\'.')
                return print('Let\'s try again, ' + name + '!')
            else:
                print('\'' + answer + '\'' + ' is wrong answer ;(. Correct answer was \'no\'.')
                return print('Let\'s try again, ' + name + '!')
    print('Congratulations, ' + name + '!')


def main():
    brain_even()


if __name__ == '__main__':
    main()
