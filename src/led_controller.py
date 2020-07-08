from src.strip import Strip
from src.mic import Mic
from src.modes import *
from constants import *
from utils.logging import Log

log = Log()

class LedController:
    def __init__(self, pin, num_leds, mic=None):
        self.mic = mic
        self.strip = Strip(pin, num_leds)
        self.strip.setMode(Arm(self.strip))
        self.strip.animate()

    def change_mode(self, mode_id):
        self.strip.terminate()
        if mode_id == None:
            print("recieve empty mode id")
            return -1
        if mode_id == "off":
            self.strip.setMode(Off(self.strip))
        if mode_id == "on":
            self.strip.setMode(On(self.strip))
        if mode_id == "rainbow_run":
            self.strip.setMode(RainbowRun(self.strip))
        log.d("Controller", "Mode set to %s" % mode_id)
        self.strip.animate()

    def off(self):
        self.change_mode("off")

    def on(self):
        self.change_mode("on")
