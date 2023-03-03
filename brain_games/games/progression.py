from random import randint

MIN_START = 1
MAX_START = 30
MIN_INTERVAL = 1
MAX_INTERVAL = 10
MIN_LENGTH = 5
MAX_LENGTH = 10
RULE = 'What number is missing in the progression?'


def our_progression(start, interval, length):
    stop = start + (length * interval)
    numbers_list = []
    for index in range(start, stop, interval):
        numbers_list.append(index)
    return numbers_list

def game_plan():
    start = randint(MIN_START, MAX_START)
    interval = randint(MIN_INTERVAL, MAX_INTERVAL)
    length =  randint(MIN_LENGTH, MAX_LENGTH)
    progression = our_progression(start, interval, length)
    hidden_index = randint(0, len(progression) - 1)
    right_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, right_answer
