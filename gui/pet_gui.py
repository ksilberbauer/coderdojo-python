import simplegui as gui
from random import randint

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

MOODS = [HAPPY, CONTENT, GRUMPY]

chance_hungry = 0.1

def random_sample(l, K):
    return [ mylist[i] for i in sorted(random.sample(xrange(len(l)), K)) ]

def get_string_input(prompt):
    user_input = None
    while not user_input:
        user_input = input(prompt)
    return user_input

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

def set_pet_hunger(pet, chance_hungry):
    if not pet["is_hungry"]:
        random_roll = randint(1, 100) / 100.0
        if random_roll <= chance_hungry:
            pet["is_hungry"] = True
            chance_hungry = 0.1 # reset chance hungry to 10%
        else:
            chance_hungry += 0.1 # increase chance hungry by 10% 

pet = {
    "age": 0,
    "is_hungry": False,
    "mood": CONTENT,
    "mood_score": 0,
    "name": (input("What is your pet's name?") or "Fluffy")
}

favorite_foods = input("What are your pet's favorite foods? (comma-separated list)") or "milk, sugar, pizza"
pet["favorite_foods"] = [food.strip() for food in favorite_foods.split(',')]

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
        pet["mood_score"] += 1 # TODO: adjust this via a play() method
    else:
        pet["mood_score"] -= 1

def timer_handler():
    global pet, chance_hungry
    pet["age"] += 1
    set_pet_hunger(pet, chance_hungry)

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

# create gui
frame = gui.create_frame("My Pet", CANVAS_WIDTH, CANVAS_HEIGHT, FRAME_WIDTH)

# output label
frame.add_input("Feed pet:", text_input_handler, INPUT_WIDTH_LARGE)

# draw image and start
frame.set_draw_handler(draw_pet)
frame.start()
timer = gui.create_timer(TIME_INTERVAL, timer_handler)
timer.start()