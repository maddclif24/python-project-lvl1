import prompt

ROUNDS = 3


def ask_and_check_answer(game, user_name):
    for _ in range(ROUNDS):
        (question, correct_answer) = game()

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'.''')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
