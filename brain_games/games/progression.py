from random import randint
RULE = 'What number is missing in the progression?'


def generate_data():
    start  = randint(1, 20)
    step = randint(1, 10)
    result = list(range(randint(0, 9), start, step))[ :5]
    random_index = randint(0, len(result) -1)
    right_answer = result[random_index]
    result[random_index] = '..'
    question = ' '.join(map(str, (result)))
    return question, str(right_answer)

