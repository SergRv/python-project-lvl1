import random


def get_quest():
    return 'What number is missing in the progression?'


def start_round():

    step = random.randint(2, 8)
    numb = random.randint(0, 15)
    progression_list = list(range(numb, 65, step))
    rand_numb = random.choice(progression_list)
    result_list = []
    for i in progression_list:
        i = str(i)
        if i == str(rand_numb):
            i = '..'
        result_list.append(i)
    question = f'{" ".join(result_list)}'

    return question, str(rand_numb)
