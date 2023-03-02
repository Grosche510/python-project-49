from random import randint
import math

MIN_RANGE = 1
MAX_RANGE = 100
RULE = 'Find the greatest common divisor of given numbers.'


def game_plan():
    number1 = randint(MIN_RANGE, MAX_RANGE)
    number2 = randint(MIN_RANGE, MAX_RANGE)
    question = f'{number1} {number2}'
    right_answer = str(math.gcd(number1, number2))
    return question, right_answer
