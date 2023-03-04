#!/usr/bin/env python3
from brain_games.games.even import make_task
from brain_games.move import ask_questions_and_get_result


def main():
    ask_questions_and_get_result(make_task)


if __name__ == '__main__':
    main()
