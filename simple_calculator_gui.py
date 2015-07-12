import simplegui as gui

canvas_w = 100
canvas_h = 200
input_small_w = 50
text_initial_y = 20
text_y_offset = 20
equal_line_w = 50

operand_1_coords = (canvas_w / 2, text_initial_y)
operand_2_coords = (canvas_w / 2, text_initial_y + text_y_offset)
operator_coords = (canvas_w / 3, text_initial_y + text_y_offset)
equal_line_points = [
    (canvas_w / 2 - 20, text_initial_y + text_y_offset + 10),
    (canvas_w / 2 + equal_line_w - 20, text_initial_y + text_y_offset + 10)
    ]

do_calculate = False
# ÷

def noop_handler(_):
    pass # do nothing when user hits ENTER

def calculate():
    global do_calculate
    do_calculate = True

def print_calculation(canvas):
    canvas.draw_text(operand_1.get_text(), operand_1_coords, 20, 'Red')
    canvas.draw_text(operand_2.get_text(), operand_2_coords, 20, 'Red')
    canvas.draw_text(operator.get_text(), operator_coords, 20, 'Gray')
    if do_calculate:
        canvas.draw_line(equal_line_points[0], equal_line_points[1], 2, 'Gray')

    
frame = gui.create_frame("Simple Calculator", canvas_w, canvas_h)

operand_1 = frame.add_input("Enter number:", noop_handler, input_small_w)
operator = frame.add_input(
    "Enter operator (+, -, *, /):", noop_handler, input_small_w)
operand_2 = frame.add_input("Enter number:", noop_handler, input_small_w)

frame.add_button("Calculate", calculate)

frame.set_draw_handler(print_calculation)

frame.start()