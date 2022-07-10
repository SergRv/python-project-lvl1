import random


def get_quest():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def counted():
    rand_numb = random.randint(1, 20)
    print(f'Question: {rand_numb}')
    if rand_numb % 2 == 0:
        return 'yes'
    else:
        return 'no'
