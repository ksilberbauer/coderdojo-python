import simplegui as gui
from random import randint, choice

FRAME_WIDTH = 500
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 400
INPUT_WIDTH_LARGE = 200
INPUT_WIDTH_SMALL = 100
TIME_INTERVAL = 1000

# TODO: image urls
KID = gui.load_image('')
KID_HUNGRY = gui.load_image('')
ADULT = gui.load_image('')
ADULT_HUNGRY = gui.load_image('')

HAPPY = "happy"
CONTENT = "content"
GRUMPY = "grumpy"

RANDOM_WORDS = ['declare', 'bareknuckled', 'cactus', 'tender', 'layer', 'will', 'photo', 'consecutive', 'rummage', 'approximating', 'henchman', 'emphasized', 'rose', 'glimpse', 'philosophical', 'iguana', 'adjective', 'microscopic', 'jill', 'trusting', 'multiply', 'parsimony', 'sublime', 'chaos', 'cryptography', 'subtle', 'squelch', 'nectar', 'immigrated', 'luke', 'postulated', 'undisclosed', 'thread', 'caramelizing', 'canary', 'flinch', 'hartford', 'candidly', 'democracy', 'bike', 'gymnasium', 'stormy', 'tinker', 'overjoyed', 'gravel', 'progressionist', 'microcircuit', 'oval', 'chain', 'harden', 'translator', 'uncle', 'telegrammatic', 'agnostic', 'outside', 'summer', 'tree']

# static functions
def random_sample(l, K):
    return [ mylist[i] for i in sorted(random.sample(xrange(len(l)), K)) ]

def get_pet_image(pet):
    # TODO: return a different pet image depending on: (1) pet["age"], (2) pet["is_hungry"]

def set_pet_hunger(pet):    
    if not pet["is_hungry"]:
        random_roll = randint(1, 100) / 100.0
        if random_roll <= pet["chance_hungry"]:
            pet["is_hungry"] = True
            pet["chance_hungry"] = 0.1 # reset chance hungry to 10%
        else:
            pet["chance_hungry"] += 0.1 # increase chance hungry by 10% 

def set_pet_mood(pet):
    # TODO: if pet["mood_score"] is 5 or more, increase pet's mood
    # TODO: if pet["mood_score"] is -5 or less, decrease pet's mood

def create_pet(name, favorite_foods):
    # TODO: add more fun properties to pet!
    # BONUS: think of cool functions you can do with those properties
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
    # TODO: check if the text is one of pet["favorite_foods"]...
    # ... if it is, make pet not hungry
    # ... if it isn't, decrease the pet["mood_score"]
    
def timer_handler():
    global pet
    # TODO: make pet age
    # TODO: set pet's hunger
    # TODO: set pet's mood
    
def play():
    # TODO: come up with a game you can play with your pet...
    # ... if you win, increase pet["mood_score"]

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
# TODO: take user input for pet's name + favorite foods
name = 
favorite_foods =
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