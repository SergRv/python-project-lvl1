import random
import math
from brain_games.games.calc import BEGIN_VALUE, FINAL_VALUE


def get_quest():
    return 'Find the greatest common divisor of given numbers.'


def start_round():

    first_numb = random.randint(BEGIN_VALUE, FINAL_VALUE)
    second_numb = random.randint(BEGIN_VALUE, FINAL_VALUE)
    question = f'{str(first_numb)} {str(second_numb)}'

    return question, str(math.gcd(first_numb, second_numb))
