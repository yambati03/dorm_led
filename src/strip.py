from src.modes import *
from constants import *
import board
import neopixel
import numpy as np
import time
import colorsys

class Strip:
    def __init__(self, pin, num_leds):
        self.mode = None
        self.num_leds = num_leds
        self.pin = pin
        self.pixels = neopixel.NeoPixel(pin, num_leds, brightness=1.0, auto_write=False)

    def setMode(self, mode):
        self.mode = mode

    def animate(self):
        self.mode.animate()

    def terminate(self):
        self.mode.terminate()

    def setLEDS(self, arr):
        for pixel in range(self.num_leds):
            self.pixels[pixel] = arr[pixel].toTuple()

    def fill(self, color):
        self.pixels.fill(color.toTuple())

    def show(self):
        self.pixels.show()

    def setBrightness(self, b):
        self.pixels.brightness = b
