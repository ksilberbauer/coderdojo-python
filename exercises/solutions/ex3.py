secret_word = input("Enter a secret word:")
guess = ""
guessed_letters = ""
correct_letters = ""

emergency_break = 0 # you'll thank me later ;)

correct_guesses = ""
for letter in secret_word:
	guess = ""
	incorrect_guesses = ""
    while guess is not letter and emergency_break < 100:
        incorrect_guesses += guess
    	print "Incorrect guesses: " + incorrect_guesses
    	guess = input("Guess the next letter:")
    	emergency_break += 1
    correct_guesses += guess
    print "Word so far: " + correct_guesses
 
print "You got it!"