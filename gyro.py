from pyjoycon import GyroTrackingJoyCon, get_L_id
import time


class GyroTracking:

    def __init__(self):
        self.joycon_id = get_L_id()
        self.joycon = GyroTrackingJoyCon(*self.joycon_id)
        self.neutral = bool

    def rotation(self):
        self.neutral_return()
        if 2 < self.joycon.rotation.x < 3.5:
            if self.neutral:
                self.neutral = False
                return True

    def neutral_return(self):
        if 0 < self.joycon.rotation.x < 0.5:
            self.neutral = True

    def rotation_y(self):
        if self.joycon.rotation.y > 1:
            return True

