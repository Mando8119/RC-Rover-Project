from input import controller
import time
import requests

controller_index = 0
operator_controller = controller(controller_index)

def logic(controller):
    # Get the position of the joysticks
    left_joystick = controller.left_stick
    right_joystick = controller.right_stick

    # Check if buttons are pressed
    BTN_X = controller.x_pressed
    BTN_B = controller.b_pressed
    BTN_Y = controller.y_pressed
    BTN_A = controller.a_pressed
    # BTN_SELECT and BTN_START are toggle buttons
    BTN_SELECT = controller.select_pressed
    BTN_START = controller.start_pressed

    # Check if bumpers are pressed
    Left_Bumper = controller.btn_tl
    Right_Bumper = controller.btn_tr

    # Get the position of the triggers
    Speed_Decrease = controller.left_trigger
    Speed_Increase = controller.right_trigger

    # Convert trigger positions to speed values
    Speed_Decrease = round(- (Speed_Decrease / 2.55) * 5)
    Speed_Increase = round((Speed_Increase / 2.55) * 5)

    Neutral_Speed = 1500  # Neutral speed value

    # Calculate the final speed value
    Speed = Speed_Decrease + Neutral_Speed + Speed_Increase

    # Get the horizontal and vertical positions of the joysticks
    left_horizontal = left_joystick[0]
    right_vertical = right_joystick[1]

    # Deadzone for the joysticks
    if abs(left_horizontal) < 0.19:
        left_horizontal = 0
    if abs(right_vertical) < 0.19:
        right_vertical = 0

    # Convert joystick positions to servo displacements
    left_horizontal = round(118 - ((left_horizontal + 1) * 25))
    right_vertical = round((right_vertical + 1) * 90)

    # Create and return the packet
    packet = " ".join([str(left_horizontal), str(Speed)])
    return packet

def send_packet(packet):
    url = f"http://192.168.4.1/"  # URL of the ESP32
    try:
        response = requests.post(url, data=packet)  # Send the packet to the ESP32
        print("Response from ESP32:", response.text)  # Print the response from the ESP32
    except requests.exceptions.RequestException as e:
        print("Failed to send packet:", e)  # Print an error message if the packet fails to send

while True:
    packet = logic(operator_controller)  # Get the packet based on the controller input
    send_packet(packet) #Send the packet to the ESP32 (Comment line out if you want
                        #to test the packet without sending it to the ESP32)
    print(packet)  # Print the packet
    time.sleep(0.1)  # Delay for 0.1 seconds