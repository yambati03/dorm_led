from flask import Flask, render_template, request
import board
import time
from constants import *
from src.led_controller import LedController

app = Flask(__name__)
app.debug = True
controller = LedController(board.D18, NUM_LEDS)

@app.route('/controller', methods=['GET', 'POST'])
def mode_dropdown():
    if request.method == "POST":
        mode = request.form["selector"]
        controller.change_mode(mode)

    modes = ['rainbow_run', 'rainbow_fade', 'off', 'on']
    return render_template('app.html', modes=modes)

if __name__ == "__main__":
    app.run()
