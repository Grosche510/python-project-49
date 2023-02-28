from random import randint
import random
RULE = 'What is the result of the expression?'


def generate_data():
    operations = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = random.choice(operations)
    question = f"{number1} {operator} {number2}"
    if operator == '+':
        right_answer = number1 + number2
    elif operator == '-':
        right_answer = number1 - number2
    elif operator == '*':
        right_answer = number1 * number2
    return question, str(right_answer)
