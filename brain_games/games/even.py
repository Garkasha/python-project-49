from random import randint


def make_task():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 99)

    def is_even(question):
        return question % 2 == 0

    if is_even(question) is True:
        result = 'yes'
    else:
        result = 'no'
    return question, result, task
