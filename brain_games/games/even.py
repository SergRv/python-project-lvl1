import random
from brain_games.games.calc import BEGIN_VALUE, FINAL_VALUE


def get_quest():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def start_round():
    rand_numb = random.randint(BEGIN_VALUE, FINAL_VALUE)
    question = f'{rand_numb}'
    if rand_numb % 2 == 0:
        rand_numb = 'yes'
    else:
        rand_numb = 'no'

    return question, rand_numb
