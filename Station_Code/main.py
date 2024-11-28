import tkinter as tk
from input import controller
import time
import requests

# Function to update the speed on the GUI
def update_speed(speed):
    speed_label.config(text=f"Speed: {speed} km/h")

# Function to update the servo position on the GUI
def update_servo_position(position):
    servo_label.config(text=f"Servo Position: {position} degrees")

# Initialize the controller
try:
    controller_index = 0
    operator_controller = controller(controller_index)
except IndexError as e:
    print('Error: Controller Disconnected!')
    exit()
# Create the main window for the GUI
try:
    window = tk.Tk()
    window.title("RC Rover GUI")
    window.geometry("500x500")
    window.configure(bg="black")

    title_label = tk.Label(window, text="RC Rover GUI", bg="black", fg="purple", font=("Arial", 32))
    title_label.pack()

    # Create labels for displaying the speed and servo position
    speed_label = tk.Label(window, text="Speed: 0 km/h", bg="black", fg="white")
    speed_label.pack()

    servo_label = tk.Label(window, text="Steering Servo Position: 0 degrees", bg="black", fg="white")
    servo_label.pack()

except IndexError as e:
    print('GUI Error:', e)
    exit()

# Function to process controller input and create a data packet
def logic(controller):
    # Get the position of the joysticks
    left_joystick = controller.left_stick
    right_joystick = controller.right_stick

    # Get the position of the triggers and calculate the speed
    Speed_Decrease = controller.left_trigger
    Speed_Increase = controller.right_trigger

    # Convert trigger positions to speed values
    Speed_Decrease = round(- (Speed_Decrease / 2.55) * 1)
    Speed_Increase = round((Speed_Increase / 2.55) * 1)

    Neutral_Speed = 1500

    # Calculate the final speed value
    Speed = Speed_Decrease + Neutral_Speed + Speed_Increase

    # Update the GUI with the speed
    update_speed(Speed)

    # Get the horizontal position of the left joystick
    left_horizontal = left_joystick[0]

    # Deadzone for the joystick
    if abs(left_horizontal) < 0.19:
        left_horizontal = 0

    # Convert joystick position to servo displacement
    left_horizontal = round(118 - ((left_horizontal + 1) * 25))

    # Update the GUI with the servo position
    update_servo_position(left_horizontal)

    # Create and return the packet
    packet = " ".join([str(left_horizontal), str(Speed)])
    return packet

# Function to send the data packet to the ESP32
def send_receive_packet(packet):
    url = f"http://192.168.4.1/"  # URL of the ESP32
    try:
        response = requests.post(url, data=packet)  # Send the packet to the ESP32
        print("Message from Rover:", response.text)  # Print the response from the ESP32
    except requests.exceptions.RequestException as e:
        print("Failed to send packet:", e)  # Print an error message if the packet fails to send

# Main loop to update the controller and GUI
def main_loop():
    while True:
        packet = logic(operator_controller)  # Get the packet based on the controller input
        send_receive_packet(packet)  # Send the packet to the ESP32
        print(packet)
        time.sleep(0.1)  # Delay for 0.1 seconds

# Run the main loop in a separate thread
import threading
threading.Thread(target=main_loop).start()

# Start the GUI event loop
window.mainloop()
