from flask import Flask, render_template, request
from utils.color import Color
import board
import time
from constants import *
from src.led_controller import LedController

app = Flask(__name__)
app.debug = True
controller = LedController(board.D18, NUM_LEDS)

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    t_color = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return Color(t_color[0], t_color[1], t_color[2])

@app.route('/controller', methods=['GET', 'POST'])
def mode_dropdown():
    if request.method == "POST":
        mode = request.form["selector"]
        color = request.form["color"]
        if mode == 'solid_color':
            color = hex_to_rgb(color)
            controller.change_mode(mode, set_color = color)
        else:
            controller.change_mode(mode)

    modes = ['rainbow_run', 'rainbow_fade', 'solid_color', 'off', 'on']
    return render_template('app.html', modes=modes)

if __name__ == "__main__":
    app.run()
