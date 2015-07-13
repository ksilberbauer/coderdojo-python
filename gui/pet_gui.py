import simplegui as gui

pet_image = pet_sound = None

CANVAS_WIDTH = 200
CANVAS_ = 200
LARGE_INPUT_WIDTH = 200
SMALL_INPUT_WIDTH = 75

def start():
    global pet_image
    pet_image = gui.load_image(image_input.get_text())
    frame.start()

def play_sound():
    global pet_sound
    if pet_sound:
        pet_sound.pause()
    pet_sound = gui.load_sound(audio_input.get_text())
    pet_sound.rewind()
    pet_sound.play()

def draw_pet(canvas):
    canvas.draw_image(
        pet_image,
        (pet_image.get_width() / 2, pet_image.get_height() / 2), # center the pet image
        (pet_image.get_width(), pet_image.get_height()), # set pet image dimensions
        (CANVAS_WIDTH / 2, CANVAS_ / 2), # center the canvas
        (CANVAS_WIDTH, CANVAS_)) # set canvas dimensions

def text_input_handler():
    pass

frame = gui.create_frame("My Pet", CANVAS_WIDTH, CANVAS_)

# image
frame.set_draw_handler(draw_pet)

# text inputs
image_input = frame.add_input('Pet Image URL:', text_input_handler, LARGE_INPUT_WIDTH)
audio_input = frame.add_input('Speak Sound URL:', text_input_handler, LARGE_INPUT_WIDTH)
name_input = frame.add_input('Pet Name:', text_input_handler, SMALL_INPUT_WIDTH)
fav_foods_input = frame.add_input('Favorite Foods:', text_input_handler, LARGE_INPUT_WIDTH)

# buttons
frame.add_button('Start', start)
frame.add_button('Play Pet Sound', play_sound)

# https://pbs.twimg.com/profile_images/2546538556/lion.jpg
# http://static1.grsites.com/archive/sounds/animals/animals105.mp3