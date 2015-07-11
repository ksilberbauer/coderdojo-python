from os import system
from random import randint

def say(something):
    print('say "%s"'.format(something))

max_number = 10
first_line = 'Guess a number between 1 and {0}'.format(max_number)
print(first_line)
say(first_line)
number = randint(1, max_number)
not_solved = True

while not_solved:
    answer = int(raw_input('?'))
    you_said = 'You typed {0}'.format(answer)
    say(you_said)
    if answer > number:
        say('The number is lower')
    elif answer < number:
        say('The number is higher')
    else:
        say('You got it right!')
        not_solved = False
