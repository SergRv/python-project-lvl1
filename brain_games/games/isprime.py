import random
import math
from brain_games.games.calc import BEGIN_VALUE, FINAL_VALUE


def get_quest():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_round():
    question = random.randint(BEGIN_VALUE, FINAL_VALUE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(question):
    counter = 2
    while counter <= math.sqrt(question):
        if question % counter == 0:
            return False
            break
        counter += 1
    return True
