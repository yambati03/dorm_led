import board
from constants import *
from src.led_controller import LedController

main():
    LedController(board.D18, NUM_LEDS)

if __name__ == '__main__':
    main()
