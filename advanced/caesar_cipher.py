ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def shift_letter(letter, n):
    new_index = (ALPHABET.index(letter) + n) % len(ALPHABET)
    new_letter = ALPHABET[new_index]
    return new_letter

def shift_word(word, n):
    new_word = ""
    for letter in word:
        new_letter = shift_letter(letter, n)
        new_word += new_letter
    return new_word

def shift_message(message, n):
    word_list= message.split(" ") # split message on spaces
    new_message_list = []
    for word in word_list:
        new_word = shift_word(word, n)
        new_message_list.append(new_word)
    return str.join(" ", new_message_list)

secret_number = None
while True:
    secret_number = input("What is your secret number?")
    if not secret_number:
        break
    secret_number = int(secret_number)
    message = input("What is your secret message?")
    if not message:
        break
    print shift_message(message, secret_number)
