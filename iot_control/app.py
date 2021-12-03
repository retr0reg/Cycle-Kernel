from flask import Flask,render_template
import RPi.GPIO as GPIO
import time
import lcd1602 as lcd
import time
from luma.led_matrix.device import *
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1 or 1, block_orientation=0,rotate=0 or 0, blocks_arranged_in_reverse_order=False)
id = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setwarnings(False)
lcd.init_lcd()
time.sleep(1)
lcd.turn_light(1)
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")

@app.route("/time")
def on():
    global id
    id = 1
    '''time'''
    
    lcd.clear_lcd()
    while id!=0:
        nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
        hourtime = time.strftime('%H',time.localtime(time.time()))
        mintime = time.strftime('%M',time.localtime(time.time()))
        sectime = time.strftime('%S',time.localtime(time.time()))
        lcd.print_lcd(1,1,nowtime)
        if mintime == '59':
            if sectime == '00':
                lcd.turn_light(1)
            elif sectime  == '59':
                lcd.turn_light(0)
        time.sleep(0.2)
    return render_template("main.html")

@app.route("/print")
def print():
    global id
    id = 1
    '''printHelloWorld'''
    lcd.clear_lcd()
    #GPIO.output(20,GPIO.LOW)
    lcd.print_lcd(0,0,"Hello World")
    return render_template("main.html")

@app.route("/clear")
def clear():
    global id
    id = 0
    lcd.clear_lcd()
    return render_template("main.html")

@app.route("/left")
def left():
    for x in range(10):
        #print("drawing")
        for x in range(5):
            with canvas(device) as draw:
                text(draw, (0, 0), chr(27), fill="white")
                time.sleep(0.01)
    return render_template("main.html")
            
@app.route("/right")
def right():
    for x in range(10):
        #print("drawing")
        for x in range(4):
            with canvas(device) as draw:
                text(draw, (0, 0), chr(26), fill="white")
                time.sleep(0.01)
    return render_template("main.html")

@app.route("/line")
def line():
    for x in range(10):
        #print("drawing")
        for x in range(4):
            with canvas(device) as draw:
                text(draw, (0, 0), chr(24), fill="white")
                time.sleep(0.01)
    return render_template("main.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
