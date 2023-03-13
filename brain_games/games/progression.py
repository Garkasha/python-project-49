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

    print_progression = progression
    index = randint(0, len(progression) - 1)
    result = str(progression[index])
    print_progression[index] = ".."
    question = " ".join(map(str, print_progression))

    return question, result
