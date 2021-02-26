import random
from brain_games import engine


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1

    answer = number1 + number2

    return[question, str(answer)]


description = 'Find the greatest common divisor of given numbers.'


def launch_gcd_game():
    engine.play_game(description, get_question_and_answer)
