from constants import *
import time

#--------------ALL PASSIVE MODE CLASSES--------------
class PassiveMode:
    def __init__(self, strip):
        self.arr_pixels = [OFF for i in range(0, NUM_LEDS)]
        self.pixels = strip

class Off(PassiveMode):
    def __init__(self):
        super.__init__()

    def animate(self):
        self.pixels.fill((OFF.r, OFF.g, OFF.b))

class RainbowRun(PassiveMode):
    def __init__(self, strip):
        super.__init__(strip)

    def shift(self):
        for i in range(self.NUM_LEDS - 1, NUM_UPDATE - 1, -1):
            self.arr_pixels[i] = self.arr_pixels[i - NUM_UPDATE]

    def animate(self):
        color = RED
        while True:
            self.pixels.shift()
            color = color.nextHue()
            for i in range(NUM_UPDATE):
                self.arr_pixels[i] = color
            self.pixels.setLEDS(self.arr_pixels)
            self.pixels.show()
            time.sleep(0.03)

#--------------ALL ACTIVE MODE CLASSES--------------
class ActiveMode:
    def __init__(self, strip, mic):
        self.mic = mic
        self.arr_pixels = [OFF for i in range(0, NUM_LEDS)]
        self.pixels = strip