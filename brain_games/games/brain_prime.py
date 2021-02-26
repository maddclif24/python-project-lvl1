import random
from brain_games import engine


def is_prime(a):
    return all(a % i for i in range(2, a))


def get_question_and_answer():
    number = random.randint(2, 20)
    question = f'{number}'
    answer = 'yes' if is_prime(number) else 'no'

    return[question, answer]


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def launch_prime_game():
    engine.play_game(description, get_question_and_answer)
