import random
import math


def get_quest():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_round():

    rand_numb = random.randint(1, 100)
    question = str(rand_numb)

    def is_prime():
        prime = True
        count = 2
        while count <= math.sqrt(rand_numb):
            if rand_numb % count == 0:
                prime = False
                break
            count += 1
        return prime

    if is_prime():
        return question, 'yes'
    else:
        return question, 'no'
