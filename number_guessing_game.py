import random

MAX_NUMBER = 10
instructions = 'Guess a number between 1 and %s' % MAX_NUMBER

number = random.randint(1, MAX_NUMBER)
is_solved = False

while not is_solved:
    guess = int(input("Guess:"))
    if guess > number:
        print 'The number is lower'
    elif guess < number:
        print 'The number is higher'
    else:
        print 'You got it!'
        is_solved = True

