import simplegui as gui

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 400
INPUT_WIDTH_LARGE = 200
INPUT_WIDTH_SMALL = 100

def random_sample(l, K):
    return [ mylist[i] for i in sorted(random.sample(xrange(len(l)), K)) ]

IMAGE_URL = input("URL for image of your pet:") or "https://pbs.twimg.com/profile_images/2546538556/lion.jpg"
NAME = input("What is your pet's name?")
favorite_foods = input("What are your pet's favorite foods? (comma-separated list)")
FAVORITE_FOODS = [food.strip() for food in favorite_foods.split(',')]

def draw_pet(canvas):
    pet_image = gui.load_image(IMAGE_URL)
    canvas.draw_image(
        pet_image,
        (pet_image.get_width() / 2, pet_image.get_height() / 2), # center of original image
        (pet_image.get_width(), pet_image.get_height()), # size of original image (for scaling)
        (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 4), # position within canvas (usually centered)
        (CANVAS_WIDTH, CANVAS_HEIGHT / 2)) # size you want the image to be in the canvas (scales, as necessary)

def text_input_handler(text):
    pass

def write_output_handler(text):
    global output
    output.set_text(text)

frame = gui.create_frame("My Pet", CANVAS_WIDTH, CANVAS_HEIGHT)

frame.set_draw_handler(draw_pet)

frame.add_label("Hi, I'm " + NAME + "!")
frame.add_input("Label test:", write_output_handler, INPUT_WIDTH_LARGE)

frame.add_label("Output:")
output = frame.add_label(','.join(FAVORITE_FOODS), INPUT_WIDTH_LARGE)

frame.start()