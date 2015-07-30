import simplegui as gui
from random import randint, choice

FRAME_WIDTH = 500
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 400
INPUT_WIDTH_LARGE = 200
INPUT_WIDTH_SMALL = 100
TIME_INTERVAL = 1000

KID = gui.load_image('http://www.hollyhornerphotography.com/data/photos/238_1sa_lion_cub_4x5_8417.jpg')
KID_HUNGRY = gui.load_image('http://media.katu.com/images/131024_lion_cub_660.jpg')
ADULT = gui.load_image('http://vignette4.wikia.nocookie.net/animalcrossing/images/e/e3/Lion-013-2048x2048.jpg/revision/latest?cb=20130406213028')
ADULT_HUNGRY = gui.load_image('https://pbs.twimg.com/profile_images/2546538556/lion.jpg')

HAPPY = "happy"
CONTENT = "content"
GRUMPY = "grumpy"

RANDOM_WORDS = ['declare', 'bareknuckled', 'cactus', 'tender', 'layer', 'will', 'photo', 'consecutive', 'rummage', 'approximating', 'henchman', 'emphasized', 'rose', 'glimpse', 'philosophical', 'iguana', 'adjective', 'microscopic', 'jill', 'trusting', 'multiply', 'parsimony', 'sublime', 'chaos', 'cryptography', 'subtle', 'squelch', 'nectar', 'immigrated', 'luke', 'postulated', 'undisclosed', 'thread', 'caramelizing', 'canary', 'flinch', 'hartford', 'candidly', 'democracy', 'bike', 'gymnasium', 'stormy', 'tinker', 'overjoyed', 'gravel', 'progressionist', 'microcircuit', 'oval', 'chain', 'harden', 'translator', 'uncle', 'telegrammatic', 'agnostic', 'outside', 'summer', 'tree']

# static functions
def random_sample(l, K):
    return [ mylist[i] for i in sorted(random.sample(xrange(len(l)), K)) ]

def get_pet_image(pet):
    if pet["age"] < 18:
        if pet["is_hungry"]:
            return KID_HUNGRY
        else:
            return KID
    else:
        if pet["is_hungry"]:
            return ADULT_HUNGRY
        else:
            return ADULT

def set_pet_hunger(pet):
    if not pet["is_hungry"]:
        random_roll = randint(1, 100) / 100.0
        if random_roll <= pet["chance_hungry"]:
            pet["is_hungry"] = True
            pet["chance_hungry"] = 0.1 # reset chance hungry to 10%
        else:
            pet["chance_hungry"] += 0.1 # increase chance hungry by 10% 

def set_pet_mood(pet):
    if -5 < pet["mood_score"] < 5:
        return
    elif pet["mood_score"] >= 5:
        if pet["mood"] == GRUMPY:
            pet["mood"] = CONTENT
        else:
            pet["mood"] = HAPPY # even if already happy
    else:
        if pet["mood"] == HAPPY:
            pet["mood"] = CONTENT
        else:
            pet["mood"] = GRUMPY # even if already grumpy
    pet["mood_score"] = 0 # reset

def create_pet(name, favorite_foods):
    pet = {
        "age": 0,
        "is_hungry": False,
        "chance_hungry": 0.1,
        "mood": CONTENT,
        "mood_score": 0,
        "name": name,
        "favorite_foods": [food.strip() for food in favorite_foods.split(',')]
    }
    return pet

# gui handlers
def draw_pet(canvas):
    pet_image = get_pet_image(pet)
    canvas.draw_image(
        pet_image,
        (pet_image.get_width() / 2, pet_image.get_height() / 2), # center of original image
        (pet_image.get_width(), pet_image.get_height()), # size of original image (for scaling)
        (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 4), # position within canvas (usually centered)
        (CANVAS_WIDTH, CANVAS_HEIGHT / 2)) # size you want the image to be in the canvas (scales, as necessary)
    display_pet_props(canvas)

def text_input_handler(text):
    if text in pet["favorite_foods"]:
        pet["is_hungry"] = False        
    else:
        pet["mood_score"] -= 1

def timer_handler():
    global pet
    pet["age"] += 1
    set_pet_hunger(pet)
    set_pet_mood(pet)

def play():
    secret_word = choice(RANDOM_WORDS)
       
    correct_guesses = ""
    incorrect_guesses = ""
            
    def get_hidden(secret_word):
        hidden_word = ""
        for letter in secret_word:
            if letter in correct_guesses:
                hidden_word += letter
            else:
                hidden_word += "_"            
        return hidden_word

    def print_hidden(hidden_word):    
        print hidden_word + " (" + str(len(secret_word)) + ")"

    hidden_word = get_hidden(secret_word)
    print_hidden(hidden_word)

    while "_" in hidden_word:
        
        print "Already guessed: " + correct_guesses + incorrect_guesses
        guess = input("Guess a letter:")
        while guess in correct_guesses + incorrect_guesses:
            guess = input("Already guessed. Guess again:")
            
        if guess in secret_word:
            correct_guesses += guess
        else:
            incorrect_guesses += guess
            
        hidden_word = get_hidden(secret_word)
        print_hidden(hidden_word)

    pet["mood_score"] += 1

def display_pet_props(canvas):
    y_offset = 0
    for prop in pet:
        val = pet[prop]
        if type(val) == type([]):
            val = ', '.join(val)
        elif type(val) != type(""):
            val = str(val)
        text = prop + ": " + val
        y_offset += 15
        position = (0, CANVAS_HEIGHT / 2 + y_offset)
        canvas.draw_text(text, position, 12, "white")

# create pet
name = input("What is your pet's name?") or "Fluffy"
favorite_foods = input("What are your pet's favorite foods? (comma-separated list)") or "milk, sugar, pizza"
pet = create_pet(name, favorite_foods)

# create gui
frame = gui.create_frame(name, CANVAS_WIDTH, CANVAS_HEIGHT, FRAME_WIDTH)

# feed pet input
frame.add_input("Feed pet:", text_input_handler, INPUT_WIDTH_LARGE)

# play with pet start button
frame.add_button("Play", play)

# draw image and start
frame.set_draw_handler(draw_pet)
frame.start()
timer = gui.create_timer(TIME_INTERVAL, timer_handler)
timer.start()

# TODO: visual indicator of pet mood (maybe change canvas background color)
# TODO: mood score going down over time
# TODO: move hangman game into the gui
# TODO: quit for hangman game + check single character input