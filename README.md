# RC-Rover-Project

This is a repository for my personal RC Rover Project. I am converting a Traxxas Bandit VXL into a fully self-driving rover and planning to make the arm fully autonomous.
<center>
![Rover Gif](https://media.giphy.com/media/2yzgQzwGmAZ8s7RVkp/giphy.gif?cid=ecf05e47dtyxllc53014pv8zd1978b3vupmnt8mvmwabhiu7&ep=v1_gifs_search&rid=giphy.gif&ct=g) 
</center>

## Project Items
- Traxxas Bandit VXL
- Arduino Nano ESP32
- Laptop with capabilities to run Python and Arduino (C++) Code
- Xbox One Controller
    - This is just what I am using,
    - any connectable controller works.

## Developer Notes
- ESC | Electronic Speed Controller
    - Write 1000 Microseconds to move full speed backwards
    - Write 1500 Microseconds to stop movement (Neutral Position)
    - Write 2000 Microseconds to move full speed forwards
- Steer Servo
    - 68 Degrees is fully to the right
    - 93 Degrees is fully forward
    - 118 Degrees is fully to the left
- Power
    - ESC currently routes power to:
        - Drive Motor
        - Arduino Nano ESC32
        - Drive Servo
        - See if we can power more servos on this, would be very helpful

## TODO
- [ ] Code better visuals for the webserver
- [ ] Source Servos for Arm (also figure out how many pivot points we want)
- [ ] Order lower MAH batteries for slower drive speeds.
- [ ] Figure out how to power Servos
- [ ] 3d model Arm
- [ ] Learn inverse kinematics for [?] degree of freedom arm
- [ ] Create PCB design
- [ ] 3d model mounting plate for electronics and Arm
- [ ] Name our Rover!
- [ ] Create branches to begin testing autonomous driving and arm movement

## Finished Tasks
- [x] Introduce functionality to the triggers for the controller
- [x] Decide on how to stream the packet to the Arduino (Sent through network from LT to ESP32) (Potentially through SERIAL via network connection?!)
- [x] Initialize first test (Working steer servo with rc control)
- [x] Clean up repository (big mess)
- [x] Test new Smart Dashboard
- [x] Test drive motor (Scary! | Motor go burr)
- [x] Figure out how to power both the ESP32 and Drive_Servo
- [x] Source Servos for the project