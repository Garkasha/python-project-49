import prompt



def ask_questions (config):
    win = False

    for qr in config:
        question = qr[0]
        result = qr[1]

        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        is_right_answer = str(answer) == str(result)

        if is_right_answer:
            print('Correct!')
            win = True
        else:
            print('\'' + str(answer) + '\'' + ' is wrong answer ;(. Correct answer was\'' + str(result) + '\' .')
            win = False
            break 

    return win


def play(task, config):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print(task)

    is_player_win = ask_questions(config)
         
    if is_player_win == True:
        print('Congratulations, ' + name + '!')
    else:
        print('Let\'s try again, ' + name + '!')


      




    