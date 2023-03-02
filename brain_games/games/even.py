from random import randint

MIN_RANGE = 1
MAX_RANGE = 10
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_plan():
    unknown_number = randint(MIN_RANGE, MAX_RANGE)
    if even(unknown_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = unknown_number
    return question, right_answer


def even(unknown_number):
    return unknown_number % 2 == 0
