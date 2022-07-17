import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(get_quest, start_round):

    user_name = welcome_user()
    print(get_quest())
    round_counter = 3
    while round_counter != 0:
        question, answer = start_round()
        print(f"Question: {question}")
        your_answer = prompt.string('Your answer: ')

        if your_answer == answer:
            print('Correct!')
            round_counter -= 1
        else:
            print(f""
                  f"'{your_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'.\n"
                  f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
