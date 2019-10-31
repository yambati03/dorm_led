import board
import neopixel
import numpy as np
import time
from color import Color
import colorsys

num_update = 5
red = Color(255, 0, 0)
orange = Color(255, 160, 0)
yellow = Color(235, 255, 0)
green = Color(35, 255, 0)
l_blue = Color(0, 250, 255)
d_blue = Color(0, 30, 255)
violet = Color(135, 0, 255)
magenta = Color(255, 0, 230)
off = Color(0, 0, 0)
on = Color(255, 255, 255)
colors = [red, orange, yellow, green, l_blue, d_blue, violet, magenta]

class Strip:
	def __init__(self, num_leds, mic):
		self.mic = mic
		self.NUM_LEDS = num_leds
		self.pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1.0, auto_write=False)
		self.on = True
		self.leds = [off for i in range(0, num_leds)]

	def toggle(self):
		if self.on == True:
			self.pixels.fill((off.r, off.g, off.b))
			self.on = False
		else:
			self.pixels.fill((on.r, on.g, on.b))
			self.on = False

	def set(self, i, color):
		self.pixels[i] = (color.r, color.g, color.b)
		self.pixels.show()

	def setRange(self, start, end, color):
		for i in range(start, end + 1):
			self.pixels[i] = (color.r, color.g, color.b)

	def setAll(self, color):
		self.pixels.fill((color.r, color.g, color.b))

	def setBrightness(self, b):
		self.pixels.brightness = b

	def pulseOnce(self):
		for i in np.arange(0.1, 1.1, 0.1):
			self.setBrightness(i)
			self.pixels.show()
		for i in np.arange(1.0, 0, -0.1):
			self.setBrightness(i)
			self.pixels.show()

	def pulse(self, num):
		for i in range(num):
			self.pulseOnce()
			time.sleep(1)

	def pulseRainbow(self):
		while True:
			for i in colors:
				self.setAll(i)
				self.pulseOnce()
				time.sleep(0.01)

	def randColor(self):
		return colors[np.random.randint(0, 8)]

	def nextColor(self, color):
		i = colors.index(color)
		if i == len(colors) - 1:
			return colors[0]
		return colors[i + 1]

	def run(self):
		color = self.randColor()
		while True:
			color = self.nextColor(color)
			for i in range(1, self.NUM_LEDS):
				self.set(i, color)
				self.set(i - 1, off)
			color = self.nextColor(color) 
			for i in range(self.NUM_LEDS - 2, 0, -1):
				self.set(i, color)
				self.set(i + 1, off)

	def peel(self):
		while True:
			color = self.randColor()
			for i in range(0, self.NUM_LEDS):
				self.set(i, color)
			color = self.nextColor(color)
			for i in range(self.NUM_LEDS - 1, -1, -1):
				self.set(i, color)


	def rainbow(self):
		color = Color(255, 0, 0)
		self.setAll(color)
		while True:
			g = color.g
			if g == 255:
				for i in range(255, -1, -5):
					color.g = i
					self.setAll(color)
					self.setBrightness(self.mic.read())
			else:
				for i in range(0, 256, 5):
					color.g = i
					self.setAll(color)
					self.setBrightness(self.mic.read())
			r = color.r
			if r == 255:
				for i in range(255, -1, -5):
					color.r = i
					self.setAll(color)
					self.setBrightness(self.mic.read())
			else:
				for i in range(0, 256, 5):
					color.r = i
					self.setAll(color)
					self.setBrightness(self.mic.read())
			b = color.b
			if b == 255:
				for i in range(255, -1, -5):
					color.b = i
					self.setAll(color)
					self.setBrightness(self.mic.read())
			else:
				for i in range(0, 256, 5):
					color.b = i
					self.setAll(color)
					self.setBrightness(self.mic.read())

	def shift(self):
		for i in range(self.NUM_LEDS - 1, num_update - 1, -1):
			self.leds[i] = self.leds[i - num_update]

	def nextHue(self, rgb):
		h, s, v = colorsys.rgb_to_hsv(rgb.r, rgb.g, rgb.b)
		h = h * 360
		if h < 360:
			h = h + 6 
		else:
			h = 0
		r, g, b = colorsys.hsv_to_rgb(h/360, s, v)
		color = Color(round(r), round(g), round(b))
		return (color)

	def rainbowRun(self):
		color = self.randColor()
		while True:
			self.shift()
			color = self.nextHue(color)
			for i in range(num_update):
				self.leds[i] = color
			for i in range(len(self.leds)):
				self.pixels[i] = (self.leds[i].r, self.leds[i].g, self.leds[i].b)
			self.pixels.show()
			time.sleep(0.03)

	def syncBrightness(self):
		self.setAll(Color(0, 0, 255))
		while True:
			vol = self.mic.read()
			print (vol)
			self.setBrightness(vol)
			self.pixels.show()

	def bar(self):
		color = Color(0, 0, 255)
		while True:
			vol = self.mic.read()
			self.setAll(off)
			self.setRange(0, round(vol*100), color)
			self.pixels.show()
