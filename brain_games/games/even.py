from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANGE = 1
MAX_RANGE = 10

def game_plan():
    question = randint(MIN_RANGE, MAX_RANGE)
    if question % 2 == 0:
        right_answer = True
    else:
        right_answer = False
    return question, right_answer
