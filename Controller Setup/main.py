from input import controller
import time
import requests

controller_index = 0
operator_controller = controller(controller_index)

def logic(controller):
    left_joystick = controller.left_stick
    right_joystick = controller.right_stick

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


    left_horizontal = left_joystick[0]
    right_vertical = right_joystick[1]
    if abs(left_horizontal) < 0.19:
        left_horizontal = 0
    if abs(right_vertical) < 0.19:
        right_vertical = 0 

    left_horizontal = round(93 + ((left_horizontal) * 25)) #steer servo displaces a max of 25 in either direction with 93 degrees being straight
    right_vertical = round((right_vertical + 1) * 90)

    # Create and send packet
    packet = " ".join([str(left_horizontal), str(right_vertical), str(Left_Trigger), str(Right_Trigger), str(Left_Bumper), str(Right_Bumper), str(BTN_X), str(BTN_B),
                       str(BTN_Y), str(BTN_A), str(BTN_SELECT), str(BTN_START)])
    return packet

def send_packet(packet):
    url = f"http://192.168.4.1/"
    try:
        response = requests.post(url, data = packet)
        print("Response from ESP32:", response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to send packet: ", e)
     
while True:
    packet = logic(operator_controller)
    send_packet(packet)
    print(packet)
    time.sleep(0.1)