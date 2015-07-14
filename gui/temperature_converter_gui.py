import simplegui as gui

# TODO: what other quantities can you convert? what about simple phrase translation?

def convert_cf(degrees_c):
    global fahrenheit
    degrees_f = (9.0 / 5) * float(degrees_c) + 32
    fahrenheit.set_text(round(degrees_f, 1))

def convert_fc(degrees_f):
    global celsius
    degrees_c = (5.0 / 9) * (float(degrees_f) - 32)
    celsius.set_text(round(degrees_c, 1))

frame = gui.create_frame("Temperature Converter", 200, 200, 200)

celsius = frame.add_input("Celsius", convert_cf, 50)
fahrenheit = frame.add_input("Fahrenheit", convert_fc, 50)

frame.start()