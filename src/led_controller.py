from src.strip import Strip
from src.mic import Mic
from src.modes import *
from constants import *
from web import *

class LedController:
    def __init__(self, pin, num_leds, mic=None):
        self.mic = mic
        self.strip = Strip(pin, num_leds)
        self.strip.setMode(Arm(self.strip))
        self.strip.animate()

    def change_mode(mode_id):
        if mode_id == None:
            print("recieve empty mode id")
            return -1
        if mode_id == "rainbow_run":
            self.strip.setMode(RainbowRun(self.strip))
        self.strip.animate()
