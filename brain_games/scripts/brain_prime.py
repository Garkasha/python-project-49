#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.move import ask_questions_and_get_result


def main():
    ask_questions_and_get_result(module=prime)


if __name__ == '__main__':
    main()
