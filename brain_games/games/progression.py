from random import randint
RULE = 'What number is missing in the progression?'


def game_plan():
    stop = randint(50, 100)
    interval = randint(1, 5)
    result = list(range(randint(0, 9), stop, interval))[: 5]
    hidden_index = randint(0, len(result) - 1)
    right_answer = result[hidden_index]
    result[hidden_index] = '..'
    question = ' '.join(map(str, (result)))
    return question, str(right_answer)
