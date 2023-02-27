from random import randint
RULE = 'What number is missing in the progression?'


def generate_data():
    length = randint(5, 10)
    series_num = []
    start_num  = randint(1, 100)
    series_num.append(start_num)
    interval = randint(1, 5)
    while len(series_num) < length:
          series_num.append(series_num[-1] + interval)
    random_index = randint(0, len(series_num) -1)
    right_answer = series_num[random_index]
    result = series_num
    result[random_index] = '..'
    question = ' '.join(map(str, series_num)) 
    return question, right_answer

