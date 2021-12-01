from flask import Flask,render_template
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setwarnings(False)

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")

@app.route("/on")
def on():
    GPIO.output(20,GPIO.HIGH)
    return render_template("main.html")

@app.route("/off")
def off():
    GPIO.output(20,GPIO.LOW)
    return render_template("main.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
