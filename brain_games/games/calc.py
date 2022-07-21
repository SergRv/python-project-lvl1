import random


BEGIN_VALUE = 1
FINAL_VALUE = 50


def get_quest():
    return 'What is the result of the expression?'


def start_round():
    first_num = random.randint(BEGIN_VALUE, FINAL_VALUE)
    second_num = random.randint(BEGIN_VALUE, FINAL_VALUE)
    rand_operator = random.choice(['+', '-', '*'])

    question = f"{str(first_num)} {str(rand_operator)} {str(second_num)}"

    if rand_operator == '+':
        result = first_num + second_num
    elif rand_operator == '-':
        result = first_num - second_num
    elif rand_operator == '*':
        result = first_num * second_num

    return question, str(result)
