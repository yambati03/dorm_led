from src.strip import Strip
from src.mic import Mic
from src.modes import *
from constants import *

mic = Mic()
strip = Strip(NUM_LEDS)
strip.setMode(RainbowRun(strip))
strip.animate()