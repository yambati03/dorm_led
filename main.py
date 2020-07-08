import board
from constants import *
from src.led_controller import LedController

def main():
    controller = LedController(board.D18, NUM_LEDS)
    controller.change_mode("rainbow_run")
    print("main thread")

if __name__ == '__main__':
    main()
