from constants import *
import time

#--------------ALL PASSIVE MODE CLASSES--------------
class PassiveMode:
    def __init__(self, strip):
        self.arr_strip = [OFF for i in range(0, NUM_LEDS)]
        self.strip = strip

class Arm(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def animate(self):
        for i in range(2):
            self.strip.fill(ON)
            self.strip.show()
            time.sleep(0.5)
            self.strip.fill(OFF)
            self.strip.show()
            time.sleep(0.5)

class Off(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def animate(self):
        self.strip.fill(OFF)

class On(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def animate(self):
        self.strip.fill(ON)

class RainbowRun(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def shift(self):
        for i in range(NUM_LEDS - 1, NUM_UPDATE - 1, -1):
            self.arr_strip[i] = self.arr_strip[i - NUM_UPDATE]

    def animate(self):
        color = RED
        while True:
            self.shift()
            color = color.nextHue()
            for i in range(NUM_UPDATE):
                self.arr_strip[i] = color
            self.strip.setLEDS(self.arr_strip)
            self.strip.show()
            time.sleep(0.03)

#--------------ALL ACTIVE MODE CLASSES--------------
class ActiveMode:
    def __init__(self, strip, mic):
        self.mic = mic
        self.arr_strip = [OFF for i in range(0, NUM_LEDS)]
        self.strip = strip
