import random
from brain_games import engine


def get_question_and_answer():
    question = random.randint(0, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return[question, answer]


description = 'Answer "yes" if the number is even, otherwise answer "no"'


def launch_even_game():
    engine.play_game(description, get_question_and_answer)
