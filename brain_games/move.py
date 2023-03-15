import prompt


ROUNDS = 3


def launch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, result = game.make_task()
        print(f"Question: {question}")
        print(result)
        answer = prompt.string('Your answer: ')

        if answer == result:
            print('Correct!')

        else:
            print(f'Answer "{answer}" is wrong answer ;(. \
Correct answer was "{result}".')
            print(f'Let\'s try again, {name}!')
            break

    else:
        print(f'Congratulations, {name}!')
