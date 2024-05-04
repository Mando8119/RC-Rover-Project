# RC-Rover-Project

This is a repository for my personal RC Rover Project. I am converting a Traxxas Bandit VXL into a fully self-driving rover and planning to make the arm fully autonomous.

## Project Items
- Traxxas Bandit VXL
- Arduino Nano ESP32
- Laptop with capabilities to run Python and Arduino (C++) Code

## TODO
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