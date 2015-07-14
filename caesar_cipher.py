LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def rot(word, n):
    return ''.join([LETTERS[(LETTERS.index(c) + n) % len(LETTERS)] for c in word])

def crypt(message, n):
    return ' '.join([rot(word, n) for word in message.split(' ') if word != ''])

secret_key = None
while secret_key != 0:
    secret_key = int(input('What is your secret key?'))
    message = input('What is your message?')
    print crypt(message, secret_key)