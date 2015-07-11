ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def play():
    LETTERS = ALL_LETTERS[:]
    word = input('Enter word to guess:').lower()
    tries = int(input('Enter # of tries:'))

    hidden = ['_' for letter in word]

    while '_' in hidden and tries > 0:
        print ''.join(hidden) + ' (%s left)' % hidden.count('_')
        guess = input('Guess a letter:')
        if guess is "None" or guess is "":
            break
        if guess in LETTERS and guess in word:
            indices = [i for i,c in enumerate(word) if c == guess]
            for i in indices:            
                hidden[i] = guess
            LETTERS.remove(guess)
        elif guess not in LETTERS:
            print 'You already guessed "%s"' % guess
        else:
            LETTERS.remove(guess)
            tries -= 1
            print 'Sorry, no "%s"' % guess

    if '_' in hidden:
        print 'Sorry, you lose'
    else:
        print 'You win!'

    if input('Enter "y" to play again:').lower() == 'y':
        play()

play()