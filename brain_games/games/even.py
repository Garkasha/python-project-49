from random import randint
from brain_games.move import ask_questions_and_get_result


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def make_task():
    question = randint(1, 99)

    def is_even(question):
        return question % 2 == 0

    if is_even(question) is True:
        result = 'yes'
    else:
        result = 'no'
    return question, result


ask_questions_and_get_result(make_task, task)
