import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_parity():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        rand_numb = random.randint(1, 20)
        print(f'Question: {rand_numb}')

        if rand_numb % 2 == 0:
            rand_numb = 'yes'
        else:
            rand_numb = 'no'
        your_answer = prompt.string('Your answer: ')

        if your_answer == rand_numb:
            print('Correct!')
            count += 1
        else:
            print(f"\'{your_answer}\' is wrong answer ;(. Correct answer was \'{rand_numb}\'.\nLet's try again, {user_name}!")
            break
        if count == 3:
            print(f'Congratulations, {user_name}!')
            break


def main():
    check_parity()


if __name__ == '__main__':
    main()
