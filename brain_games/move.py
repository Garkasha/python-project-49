import prompt


def ask_questions_and_get_result(module):
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(module.DESCRIPTION)

    while counter < 3:
        question, result = module.make_task()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        is_right_answer = str(answer) == str(result)

        if is_right_answer:
            print('Correct!')
            counter += 1
        else:
            print('\'' + str(answer) + '\'' + ' is \
wrong answer ;(. Correct answer was\'' + str(result) + '\' .')

            print('Let\'s try again, ' + name + '!')
            break

        if counter == 3:
            print('Congratulations, ' + name + '!')
