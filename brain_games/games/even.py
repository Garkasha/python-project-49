from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_task():
    question = randint(1, 99)

    def is_even(question):
        return question % 2 == 0

    if is_even(question) is True:
        result = 'yes'
    else:
        result = 'no'
    return question, result
