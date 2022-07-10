import random


def get_quest():
    print('What is the result of the expression?')


def counted():
    first_num = random.randint(1, 20)
    second_num = random.randint(1, 20)
    rand_operator = random.choice(['+', '-', '*'])
    print(f'Question: {str(first_num)} {str(rand_operator)} {str(second_num)}')

    if rand_operator == '+':
        result = first_num + second_num
    elif rand_operator == '-':
        result = first_num - second_num
    elif rand_operator == '*':
        result = first_num * second_num

    return str(result)
