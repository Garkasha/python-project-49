from random import randint
from brain_games.move import ask_questions_and_get_result

def task():
    print('Answer "yes" if the nomber is prime, otherwise answer "no".')

def make_task():
    number = randint(2, 99)

    def is_prime(number):
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False

    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'

    question = number
    
    return question, result

ask_questions_and_get_result(make_task, task)
