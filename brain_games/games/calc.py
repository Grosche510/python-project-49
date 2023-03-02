from random import randint
import random

RULE = 'What is the result of the expression?'
MIN_RANGE = 1
MAX_RANGE = 10
OPERATION1 = '+'
OPERATION2 = '-'
OPERATION3 = '*'

def game_plan():
    operations = [OPERATION1, OPERATION2, OPERATION3]
    number1 = randint(MIN_RANGE, MAX_RANGE)
    number2 = randint(MIN_RANGE, MAX_RANGE)
    operator = random.choice(operations)
    question = f"{number1} {operator} {number2}"
    if operator == '+':
        right_answer = number1 + number2
    elif operator == '-':
        right_answer = number1 - number2
    elif operator == '*':
        right_answer = number1 * number2
    return question, str(right_answer)
