import prompt


def launch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.DESCRIPTION)

    for i in range(3):
        question, result = game.make_task()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        is_right_answer = str(answer) == str(result)

        if is_right_answer:
            print('Correct!')

        else:
            print('\'' + str(answer) + '\'' + ' is \
wrong answer ;(. Correct answer was\'' + str(result) + '\' .')
            print('Let\'s try again, ' + name + '!')
            break

        if i == 2:
            print('Congratulations, ' + name + '!')
