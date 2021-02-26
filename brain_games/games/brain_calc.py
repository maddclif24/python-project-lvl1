import random
from brain_games.engine import play_game

OPERATIONS = {1: '+', 2: "-", 3: "*"}


def get_question_and_answer():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operation = OPERATIONS[random.randint(1, 3)]
    question = f'{operand1} {operation} {operand2}'

    if operation == '+':
        answer = operand1 + operand2
    elif operation == '-':
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2

    return[question, str(answer)]


description = 'What is the result of the expression?'


def launch_calc_game():
    play_game(description, get_question_and_answer)
