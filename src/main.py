import board 
from strip import * 
from color import Color
from mic import Mic

mic = Mic()
strip = Strip(150, mic)

strip.bar()
