import random
import math


def get_quest():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def counted():

    rand_numb = random.randint(1, 100)
    prime = True
    count = 2
    print(rand_numb)
    while count <= math.sqrt(rand_numb):
        if rand_numb % count == 0:
            prime = False
            break
        count += 1

    if prime:
        return 'yes'
    else:
        return 'no'
