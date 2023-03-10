from random import randint
import math
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def game_plan():
    question = randint(1, 10)
    number = question
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
