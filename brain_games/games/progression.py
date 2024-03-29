import random
from brain_games import start_game


BEGIN_STEP = 2
FINAL_STEP = 8
BEGIN_RANDOM_NUMB = 0
FINAL_RANDOM_NUMB = 15


GAME_QUEST = 'What number is missing in the progression?'


def start_round():

    step = random.randint(BEGIN_STEP, FINAL_STEP)
    numb = random.randint(BEGIN_RANDOM_NUMB, FINAL_RANDOM_NUMB)
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


def run_this_game():
    start_game.play_game(GAME_QUEST, start_round)
