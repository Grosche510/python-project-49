from random import randint
from random import choice

RULE = 'What is the result of the expression?'
MIN_RANGE = 1
MAX_RANGE = 10
OPERATION1 = '+'
OPERATION2 = '-'
OPERATION3 = '*'

def game_plan():
    operator =choice([OPERATION1, OPERATION2, OPERATION3])
    number1 = randint(MIN_RANGE, MAX_RANGE)
    number2 = randint(MIN_RANGE, MAX_RANGE)
    question = f"{number1} {operator} {number2}"
    right_answer = str(calculate(number1, number2, operator))
    return question, right_answer

def calculate(number1, number2, operations):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    return result
