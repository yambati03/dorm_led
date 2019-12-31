from src.modes import *
from constants import *
import board
import neopixel
import numpy as np
import time
import colorsys

class Strip:
    def __init__(self, num_leds):
        self.mode = None
        self.num_leds = num_leds
        self.pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1.0, auto_write=False)

    def setMode(self, mode):
        self.mode = mode

    def animate(self):
        self.mode.animate()

    def setLEDS(self, arr):
        for pixel in range(self.num_leds):
            self.pixels[pixel] = arr[pixel]

    def show(self):
        self.pixels.show()

    def setBrightness(self, b):
        self.pixels.brightness = b