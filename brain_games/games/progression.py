from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_task():
    progression = []
    start_progression = randint(0, 50)
    step_progression = randint(1, 9)
    progression.append(start_progression)

    for i in range(0, randint(5, 10)):
        next_number = progression[-1] + step_progression
        progression.append(next_number)

    index = randint(0, len(progression) - 1)
    result = str(progression[index])
    progression[index] = ".."
    question = " ".join(map(str, progression))

    return question, result
