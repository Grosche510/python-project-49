import prompt
ATTEMPTS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for _ in range(ATTEMPTS):
        question, right_answer = game.game_plan()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f'\"{answer}\" is wrong answer ;(.'f' Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
        print(f'Congratulations, {name}!')
