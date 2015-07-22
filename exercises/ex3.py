secret_word = input("Enter a secret word:")
guess = ""
guessed_letters = ""
correct_letters = ""

emergency_break = 0 # you'll thank me later ;)

# TODO: the goal is to ask the user to guess each letter in the secret_word, one at a time
for letter in secret_word:
    while guess is not letter and emergency_break < 100:
        # TODO: keep track of all the incorrect guesses, and print them for the user as they guess
        emergency_break += 1
    # TODO: keep track of the correct guesses, and print the (partial) word each time the user guesses a new letter correctly

  
 
print "You got it!"