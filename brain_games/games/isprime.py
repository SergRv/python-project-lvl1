import random
import math
from brain_games.games.calc import BEGIN_VALUE, FINAL_VALUE
from brain_games import start_game


GAME_QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_round():
    question = random.randint(BEGIN_VALUE, FINAL_VALUE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(question):
    counter = 2
    while counter <= math.sqrt(question):
        if question % counter == 0:
            return False
        counter += 1
    return True

def run_this_game():
    start_game.play_game(GAME_QUEST, start_round)
