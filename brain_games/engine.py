import prompt

rounds_count = 3


def ask_question_get_answer(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def play_round(player_name, get_question_and_answer):
    correct_answer_count = 0
    while correct_answer_count < rounds_count:
        [question, answer] = get_question_and_answer()
        player_answer = ask_question_get_answer(question)
        if player_answer != answer:
            print(f'''\'{player_answer}\' is wrong answer ;(. \
Correct answer was \'{answer}\'.''')
            print(f"Let's try again, {player_name}!")
            return
        print('Correct!')
        correct_answer_count += 1
    print(f'Congratulation, {player_name}!')


def play_game(description, question_and_answer):
    greeting = 'Welcome to the Brain Games!'
    print(greeting)
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    print(description)
    play_round(player_name, question_and_answer)
