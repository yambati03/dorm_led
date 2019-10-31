import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class Mic:
	def __init__(self): 
		self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

		self.cs = digitalio.DigitalInOut(board.D22)

		self.mcp = MCP.MCP3008(self.spi, self.cs)

		self.chan0 = AnalogIn(self.mcp, MCP.P0)

		self.last_read = 0
		self.tolerance = 300

	def remap_range(self, value, left_min, left_max, right_min, right_max):
		left_span = left_max-left_min
		right_span = right_max-right_min

		value_scaled = (value - left_min) / (left_span)

		return round(right_min + (value_scaled * right_span), 2)

	def read(self):
		left = 10000
		right = 65535
		input = self.chan0.value

		adjust_in = abs(input - self.last_read)

		if adjust_in > self.tolerance:
			self.last_read = input
			return(self.remap_range(input, left, right, 0, 1))
		else:
			return(self.remap_range(self.last_read, left, right, 0, 1))
