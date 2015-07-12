import simplegui as gui

canvas_w = 100
canvas_h = 200
input_small_w = 50
text_initial_y = 20
text_y_offset = 20
equal_line_w = 50
answer = ""

arg_1_coords = (canvas_w / 2, text_initial_y)
arg2_coords = (canvas_w / 2, text_initial_y + text_y_offset)
operator_coords = (canvas_w / 3, text_initial_y + text_y_offset)
equal_line_points = [
    (canvas_w / 2 - 20, text_initial_y + text_y_offset + 10),
    (canvas_w / 2 + equal_line_w - 20, text_initial_y + text_y_offset + 10)]
answer_coords = (canvas_w / 2, text_initial_y + text_y_offset * 2)

do_calculate = False
# ÷

def noop_handler(_):
    pass # do nothing when user hits ENTER

def calculate():
    global do_calculate, answer
    do_calculate = True
    arg1 = float(arg_1.get_text())
    arg2 = float(arg_2.get_text())
    op = operator.get_text()
    answer = do_math(arg1, arg2, op)


def do_math(arg1, arg2, op):
    if op is '+':
        return arg1 + arg2
    elif op is '-':
        return arg1 - arg2
    elif op is '*':
        return arg1 * arg2
    elif op is '/':
        return arg1 / arg2

def print_calculation(canvas):
    canvas.draw_text(arg_1.get_text(), arg_1_coords, 20, 'Red')
    canvas.draw_text(arg_2.get_text(), arg2_coords, 20, 'Red')
    canvas.draw_text(operator.get_text(), operator_coords, 20, 'Gray')
    if do_calculate:
        canvas.draw_line(equal_line_points[0], equal_line_points[1], 2, 'Gray')
    canvas.draw_text(str(answer), answer_coords, 20, 'Green')

    
frame = gui.create_frame("Simple Calculator", canvas_w, canvas_h)

arg_1 = frame.add_input("Enter number:", noop_handler, input_small_w)
operator = frame.add_input(
    "Enter operator (+, -, *, /):", noop_handler, input_small_w)
arg_2 = frame.add_input("Enter number:", noop_handler, input_small_w)

frame.add_button("Calculate", calculate)

frame.set_draw_handler(print_calculation)

frame.start()