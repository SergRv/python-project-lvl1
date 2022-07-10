import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def started_game(get_quest, counted):

    user_name = welcome_user()
    get_quest()
    count = 0
    while count != 3:
        begin_game = counted()
        your_answer = prompt.string('Your answer: ')

        if your_answer == begin_game:
            print('Correct!')
            count += 1
        else:
            print(f""
                  f"'{your_answer}' is wrong answer ;(."
                  f" Correct answer was '{begin_game}'.\n"
                  f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
