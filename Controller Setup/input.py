import inputs
import threading

#index is the controller value [First controller: 0, Second Controller: 1, etc.]
class controller:
    def __init__(self, index):
        self.right_stick = (0, 0)
        self.left_stick = (0, 0)
        self.right_trigger = 0
        self.left_trigger = 0
        self.a_pressed = 0
        self.x_pressed = 0
        self.b_pressed = 0
        self.y_pressed = 0
        self.select_pressed = 0
        self.start_pressed = 0
        self.btn_tl = 0
        self.btn_tr = 0
        self.device = inputs.devices.gamepads[index]
        self._thread()
        self.select_toggle = False
        self.start_toggle = False
    def _run(self):
        while True:
            for event in self.device.read():
                match str(event.code):
                    case "ABS_X":
                        self.left_stick = (event.state / 32768, self.left_stick[1])
                        break
                    case "ABS_Y":
                        self.left_stick = (self.left_stick[0], event.state / 32768)
                        break
                    case "ABS_RX":
                        self.right_stick = (event.state / 32768, self.right_stick[1])
                        break
                    case "ABS_RY":
                        self.right_stick = (self.right_stick[0], event.state / 32768)
                        break
                    case "BTN_SELECT":
                        if event.state == 1 and self.select_toggle == False:
                            self.select_toggle = True
                            self.select_pressed = '1'
                        elif event.state ==1 and self.select_toggle == True:
                            self.select_pressed = '0'
                            self.select_toggle = False
                        break
                    case "BTN_START":
                        if event.state == 1 and self.start_toggle == False:
                            self.start_toggle = True
                            self.start_pressed = '1'
                        elif event.state == 1 and self.start_toggle == True:
                            self.start_pressed = '0'
                            self.start_toggle = False
                        break
                    case "BTN_EAST":
                        self.b_pressed = ('1' if event.state == 1 else '0')
                        break
                    case "BTN_WEST":
                        self.x_pressed = ('1' if event.state == 1 else '0')
                        break
                    case "BTN_NORTH":
                        self.y_pressed = ('1' if event.state == 1 else '0')
                        break
                    case "BTN_SOUTH":
                        self.a_pressed = ('1' if event.state == 1 else '0')
                        break
                    case "BTN_TL":
                        self.btn_tl = ('1' if event.state == 1 else '0')                      
                        break
                    case "BTN_TR":
                        self.btn_tr = ('1' if event.state == 1 else '0')
                        break
                    case "ABS_RZ": 
                        self.right_trigger = event.state
                        break
                    case "ABS_Z":
                        self.left_trigger = event.state
                        break
                    case "SYN_REPORT": 
                        #print(str(event.code) + ": " + str(event.state))
                        break
                    case _:
                        print(str(event.code) + ": " + str(event.state))
    
    def _thread(self):
        _run_thread = threading.Thread(target=self._run, daemon=True)
        _run_thread.start()