import random


def get_quest():
    print('What number is missing in the progression?')


def counted():

    step = random.randint(2, 8)
    numb = random.randint(0, 15)
    progression_list = list(range(numb, 45, step))
    rand_numb = random.choice(progression_list)
    result_list = []
    for i in progression_list:
        if i == rand_numb:
            i = '..'
        result_list.append(i)
    print('Question:',*result_list)

    return str(rand_numb)
