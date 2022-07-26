import prompt

GAME_COUNTER = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(GAME_QUEST, start_round):

    user_name = welcome_user()
    print(GAME_QUEST)
    for i in range(GAME_COUNTER):
        question, answer = start_round()
        print(f"Question: {question}")
        your_answer = prompt.string('Your answer: ')

        if your_answer == answer:
            print('Correct!')
        else:
            print(f""
                  f"'{your_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'.\n"
                  f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
