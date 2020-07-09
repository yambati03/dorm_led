from src.strip import Strip
from src.mic import Mic
from src.modes import *
from constants import *
from utils.color import Color
from utils.logging import Log

log = Log()

class LedController:
    def __init__(self, pin, num_leds, mic=None):
        self.mic = mic
        self.strip = Strip(pin, num_leds)
        self.strip.setMode(Arm(self.strip))
        self.strip.animate()

    def change_brightness(self, b):
        if 0 < b < 1:
            self.strip.setBrightness(b)

    def change_mode(self, mode_id, set_color=None):
        self.strip.terminate()
        if mode_id == "off":
            self.strip.setMode(Off(self.strip))
        elif mode_id == "on":
            self.strip.setMode(On(self.strip))
        elif mode_id == "rainbow_run":
            self.strip.setMode(RainbowRun(self.strip))
        elif mode_id == "rainbow_fade":
            self.strip.setMode(RainbowFade(self.strip))
        elif mode_id == "solid_color":
            if isinstance(set_color, Color):
                self.strip.setMode(SolidColor(self.strip, set_color))
            else:
                log.e("Controller", "Recieved invalid color")
        else:
            log.e("Controller", "Recieved invalid mode id %s" % mode_id)
            return -1
        self.strip.animate()
        log.i("Controller", "Mode set to %s" % mode_id)

    def off(self):
        self.change_mode("off")

    def on(self):
        self.change_mode("on")
