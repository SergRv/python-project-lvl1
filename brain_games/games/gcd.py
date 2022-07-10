import random
import math


def get_quest():
    print('Find the greatest common divisor of given numbers.')


def counted():

    first_numb = random.randint(1, 50)
    second_numb = random.randint(1, 50)
    print(f'Question: {str(first_numb)} {str(second_numb)}')

    return str(math.gcd(first_numb, second_numb))
