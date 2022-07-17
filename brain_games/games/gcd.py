import random
import math


def get_quest():
    return 'Find the greatest common divisor of given numbers.'


def start_round():

    first_numb = random.randint(1, 50)
    second_numb = random.randint(1, 50)
    question = f'{str(first_numb)} {str(second_numb)}'

    return question, str(math.gcd(first_numb, second_numb))
