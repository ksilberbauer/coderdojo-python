import simplegui as gui
from random import randint

FRAME_WIDTH = 500
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 400
INPUT_WIDTH_LARGE = 200
INPUT_WIDTH_SMALL = 100
TIME_INTERVAL = 1000

chance_hungry = 0.1

def random_sample(l, K):
    return [ mylist[i] for i in sorted(random.sample(xrange(len(l)), K)) ]

def get_string_input(prompt):
    user_input = None
    while not user_input:
        user_input = input(prompt)
    return user_input

pet = { "age": 0.0, "is_hungry": True }

pet["image_url"] = input("URL for image of your pet:") or "https://pbs.twimg.com/profile_images/2546538556/lion.jpg"
pet["name"] = input("What is your pet's name?") or "Fluffy"
favorite_foods = input("What are your pet's favorite foods? (comma-separated list)") or "milk, sugar, pizza"
pet["favorite_foods"] = [food.strip() for food in favorite_foods.split(',')]




# gui handlers
def draw_pet(canvas):
    print(chance_hungry) # testing
    pet_image = gui.load_image(pet["image_url"])
    canvas.draw_image(
        pet_image,
        (pet_image.get_width() / 2, pet_image.get_height() / 2), # center of original image
        (pet_image.get_width(), pet_image.get_height()), # size of original image (for scaling)
        (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 4), # position within canvas (usually centered)
        (CANVAS_WIDTH, CANVAS_HEIGHT / 2)) # size you want the image to be in the canvas (scales, as necessary)
    display_pet_props(canvas)

def text_input_handler(text):
    pass

def write_output_handler(text):
    global output
    pet["is_hungry"] = False # testing
    output.set_text(text)

def timer_handler():
    global pet, chance_hungry
    pet["age"] += 0.1
    if not pet["is_hungry"]:
        random_roll = randint(1, 100) / 100.0
        if random_roll <= chance_hungry:
            pet["is_hungry"] = True
            chance_hungry = 0.1 # reset chance hungry to 10%
        else:
            chance_hungry += 0.1 # increase chance hungry by 10%


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
frame.add_input("Label test:", write_output_handler, INPUT_WIDTH_LARGE)
frame.add_label("Output:")
output = frame.add_label(','.join(pet["favorite_foods"]), INPUT_WIDTH_LARGE)

# draw image and start
frame.set_draw_handler(draw_pet)
frame.start()
timer = gui.create_timer(TIME_INTERVAL, timer_handler)
timer.start()

# TODO: make pet picture age
# TODO: make pet hungry after a certain number of ticks
# TODO: make pet say things
# TODO: make pet do things