from input import controller
import time

controller_index = 0
operator_controller = controller(controller_index)

def logic(controller):
    x = controller.left_stick
    y = controller.right_stick

    BTN_X = controller.x_pressed
    BTN_B = controller.b_pressed
    BTN_Y = controller.y_pressed
    BTN_A = controller.a_pressed
    BTN_SELECT = controller.select_pressed
    BTN_START = controller.start_pressed

    Left_Bumper = controller.btn_tl
    Right_Bumper = controller.btn_tr

    Left_Trigger = controller.left_trigger
    Right_Trigger = controller.right_trigger


    horizontal = x[0]
    vertical = y[1]
    if abs(horizontal) < 0.19:
        horizontal = 0
    if abs(vertical) < 0.19:
        vertical = 0 

    horizontal = round((horizontal + 1) * 90)
    vertical = round((vertical + 1) * 90)

    # Create and send packet
    packet = " ".join([str(horizontal), str(vertical), str(Left_Trigger), str(Right_Trigger), str(Left_Bumper), str(Right_Bumper), str(BTN_X), str(BTN_B),
                       str(BTN_Y), str(BTN_A), str(BTN_SELECT), str(BTN_START)])
    return packet
     
while True:
    packet = logic(operator_controller)
    print(packet)
    time.sleep(0.1)