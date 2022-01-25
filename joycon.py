from pyjoycon import ButtonEventJoyCon, get_L_id


class JoyConHandler:

    def __init__(self):
        self.joycon_id = get_L_id()
        self.joycon = ButtonEventJoyCon(*self.joycon_id)
        self.pressed = set()

    def get_key_pressed(self, key):
        return key in self.pressed

    def key_pressed(self, key):
        self.pressed.add(key)
