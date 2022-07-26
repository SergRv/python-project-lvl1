import random
import math
from brain_games.games.calc import BEGIN_VALUE, FINAL_VALUE
from brain_games import start_game

GAME_QUEST = 'Find the greatest common divisor of given numbers.'


def start_round():

    first_numb = random.randint(BEGIN_VALUE, FINAL_VALUE)
    second_numb = random.randint(BEGIN_VALUE, FINAL_VALUE)
    question = f'{str(first_numb)} {str(second_numb)}'
    answer = str(math.gcd(first_numb, second_numb))

    return question, answer


def run_this_game():
    start_game.play_game(GAME_QUEST, start_round)
