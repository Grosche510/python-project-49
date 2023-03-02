from random import randint

MIN_STOP = 50
MAX_STOP = 100
MIN_INTERVAL = 1
MAX_INTERVAL = 5
MIN_RANGE = 0
MAX_RANGE = 9
RULE = 'What number is missing in the progression?'


def game_plan():
    stop = randint(MIN_STOP, MAX_STOP)
    interval = randint(MIN_INTERVAL, MAX_INTERVAL)
    result = list(range(randint(MIN_RANGE, MAX_RANGE), stop, interval))[: 5]
    hidden_index = randint(0, len(result) - 1)
    right_answer = result[hidden_index]
    result[hidden_index] = '..'
    question = ' '.join(map(str, (result)))
    return question, str(right_answer)
