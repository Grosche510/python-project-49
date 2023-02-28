from random import randint
import math
RULE = 'Answer "yes" if given number is prime, otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    else:
        return True

def generate_date():
    question = randint(1, 10)
    number = question
    if is_prime(number):
        rigth_answer = 'yes'
   else:
        rigth_answer = 'no'
   return question, right_answer