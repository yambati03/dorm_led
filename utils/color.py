import colorsys

class Color:
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

	def nextHue(self):
		h, s, v = colorsys.rgb_to_hsv(self.r, self.g, self.b)
		h = h * 360
		if h < 360:
			h = h + 6
		else:
			h = 0
		r, g, b = colorsys.hsv_to_rgb(h/360, s, v)
		color = Color(round(r), round(g), round(b))
		return (color)
