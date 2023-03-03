from random import randint

MIN_STOP = 50
MAX_STOP = 100
MIN_INTERVAL = 1
MAX_INTERVAL = 5
RULE = 'What number is missing in the progression?'


def our_progression(stop, interval, result):
    result = list(range(randint(0, 9), stop, interval))[: 5]
    return result

def game_plan():
    stop = randint(MIN_STOP, MAX_STOP)
    interval = randint(MIN_INTERVAL, MAX_INTERVAL)
    result = our_progression(stop, interval, result)
    hidden_index = randint(0, len(result) - 1)
    right_answer = str(result[hidden_index])
    result[hidden_index] = '..'
    question = ' '.join(map(str, result))
    return question, right_answer
