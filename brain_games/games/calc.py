import random


def get_quest():
    return 'What is the result of the expression?'


def start_round():
    first_num = random.randint(1, 20)
    second_num = random.randint(1, 20)
    rand_operator = random.choice(['+', '-', '*'])
    question = f"{str(first_num)} {str(rand_operator)} {str(second_num)}"

    if rand_operator == '+':
        result = first_num + second_num
    elif rand_operator == '-':
        result = first_num - second_num
    elif rand_operator == '*':
        result = first_num * second_num

    return question, str(result)
