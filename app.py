from flask import Flask,render_template
import RPi.GPIO as GPIO
import time
import lcd1602 as lcd
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
    

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
