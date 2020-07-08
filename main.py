import board
import time
from constants import *
from src.led_controller import LedController

def main():
    controller = LedController(board.D18, NUM_LEDS)
    controller.change_mode("rainbow_run")
    time.sleep(2)
    controller.change_brightness(0.5)
    time.sleep(5)
    controller.off()

if __name__ == '__main__':
    main()
