from random import randint

MIN_START = 1
MAX_START = 20
MIN_INTERVAL = 1
MAX_INTERVAL = 10
MIN_LANGTH = 5
MAX_LANGTH = 10
RULE = 'What number is missing in the progression?'


def our_progression(start, interval, length):
    stop = start + (length * interval)
    result = list(range(randint(MIN_START, MAX_START), stop, interval))
    return result

def game_plan():
    start = randint(MIN_START, MAX_START)
    interval = randint(MIN_INTERVAL, MAX_INTERVAL)
    length = randint(MIN_LANGTH, MAX_LANGTH)
    result = our_progression(start, interval, length)
    hidden_index = randint(0, len(result) - 1)
    right_answer = str(result[hidden_index])
    result[hidden_index] = '..'
    question = ' '.join(map(str, result))
    return question, right_answer
