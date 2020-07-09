from constants import *
from threading import Thread
import time

#--------------ALL PASSIVE MODE CLASSES--------------
class PassiveMode:
    def __init__(self, strip):
        self.arr_strip = [OFF for i in range(0, NUM_LEDS)]
        self.strip = strip
        self.running = True

    def terminate(self):
        self.running = False

    def animate(self):
        pass

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
        self.strip.show()

class On(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def animate(self):
        self.strip.fill(ON)
        self.strip.show()

class SolidColor(PassiveMode):
    def __init__(self, strip, color):
        super().__init__(strip)
        self.color = color

    def animate(self):
        self.strip.fill(self.color)
        self.strip.show()

class RainbowFade(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def run(self):
        color = RED
        while self.running:
            color = color.nextHue()
            self.strip.fill(color)
            self.strip.show()
            time.sleep(0.03)

    def animate(self):
        thread = Thread(target = self.run)
        thread.start()

class RainbowRun(PassiveMode):
    def __init__(self, strip):
        super().__init__(strip)

    def shift(self):
        for i in range(NUM_LEDS - 1, NUM_UPDATE - 1, -1):
            self.arr_strip[i] = self.arr_strip[i - NUM_UPDATE]

    def run(self):
        color = RED
        while self.running:
            self.shift()
            color = color.nextHue()
            for i in range(NUM_UPDATE):
                self.arr_strip[i] = color
            self.strip.setLEDS(self.arr_strip)
            self.strip.show()
            time.sleep(0.03)

    def animate(self):
        thread = Thread(target = self.run)
        thread.start()

#--------------ALL ACTIVE MODE CLASSES--------------
class ActiveMode:
    def __init__(self, strip, mic):
        self.mic = mic
        self.arr_strip = [OFF for i in range(0, NUM_LEDS)]
        self.strip = strip
