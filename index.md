# Cycle 's Kernel ![](https://img.shields.io/badge/SupportedBy-Ret1w1cky-blueviolet)
![](https://cdn.jsdelivr.net/gh/DDizzzy79/cdn/posts/144699458-1e46ac3e-5501-4b31-be10-397a87a41ed0.png)

---- **A Iot Bike system based on RaspberryPi, Arduino**  
## 0x1 What is This?
Cyclic's Kernel is an independent System With self-producing energy IoT Web control; the system's Energy Source is a 12V6W Generator. And The Voltage, Current is not concerned; now, I will introduce those stuff to You
[Plan.pdf](https://github.com/DDizzzy79/ScienceFair/files/7633868/default.pdf)  
Also, for extra info, Lots of our Code is based on lots of thoughts on the internet
## 0x2 Basic plans
Our plan includes that:  
* Generator
* Clock(Shows Velocity&Time)
* Controlled turning light
* Energy Store Device
* Other IoT Devices
# Generaters
For our Generators, We selected A **12V6WGenerater** , So Far, The maximum of it is about `5~6V.`
But, We were not excluded. That the generator can generate above 6V. So far, The generator's voltage output has exceeded our's minimum request.  
We chose to install it on the wire of the tire. It works well, and We can get 5~6v during a normal ride.
# RaspberryPi
![](https://cdn.jsdelivr.net/gh/DDizzzy79/cdn/posts/144403737-64037c69-4959-492a-bb5d-5c7ec4068d5b.png)
For our SBC (single-board Computer) We selected Raspberry Pi due to the high-functioning & Raspberry-based environment; I found a RaspberryPi 4B; by using Serial Port debugging, I successfully installed the Raspberry Linux kernel, After Then, it was a dull time of debugging & installing....... Environment. We First tried to do a basic IO In/Out Circus by coding a Python script With RPi.GIPO, also be careful when setting the IO port for BMC   

```python
import RPi.GPIO as gpio
import time

p = 11
gpio.setmode(BMC)
gpio.setup(p,gpio.OUT)

While True:
  gpio.output(p,gpio.HIGH)
  time.sleep(1)
  gpio.output(p,gpio.LOW)
  time.sleep(1)
```   

This Script will First, it will set the pin finding mode to "bmc ", then it will set the p (GPIO.11) pin to output mode; after That, Raspberry Pi is going to run the script in the `while loop` Which is set the `p` to high, Wait for 1 second set the `p` to low. Repeated and repeated.  
btw, You can set The IO pin setting by using  `gpio readall`

```shell
# root @ raspberrypi in ~ [18:49:46] 
$ gpio readall
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | OUT  | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
```

as We can see, The io pins are listed blow, thus, you can check the pins here and change the `p config` in the python script.  
And now, The module used in The `Cyclic's Kernel` Project will be introduced.

## LCD1602
  
  
   ![](https://cdn.jsdelivr.net/gh/DDizzzy79/cdn/posts/lcd.svg)  

**lcd1602 module is a python module based on internet resources**  
First of all, LCD1602 is an LCD Which contains `16*2=32` Space to type,   
>*Also, I will not explain How Send_data() & Send_command() Work, Because I don't Know How How does it work*  

**Installed Functions:**
## init_lcd()

```python
def init_lcd():
    try:
        send_command(0x33) # Must initialize to 8-line mode at first
        time.sleep(0.005)
        send_command(0x32) # Then initialize to 4-line mode
        time.sleep(0.005)
        send_command(0x28) # 2 Lines & 5*7 dots
        time.sleep(0.005)
        send_command(0x0C) # Enable display without cursor
        time.sleep(0.005)
        send_command(0x01) # Clear Screen
        BUS.write_byte(LCD_ADDR ,0x08)
    except:
        return False
    else:
        return True
```

This function doesn't require any arguments, it just simply initial the LCD1602
## clear_lcd()
```python
def clear_lcd():
    send_command(0x01) # Clear Screen
```

This function will clean the LCD1602's screen by calling `send_data()` function, basically it is just sending a message to LCD1602.
## print_lcd()
```python
def print_lcd(x, y, str):
    if x < 0:
        x = 0
    if x > 15:
        x = 15
    if y <0:
        y = 0
    if y > 1:
        y = 1
 
    # Move cursor
    addr = 0x80 + 0x40 * y + x
    send_command(addr)
     
    for chr in str:
        send_data(ord(char))
```
for This function, it requires 3 argruments which is `x`,`y',`str` Which I will expain first:  
* **X**,The x coordinate That the `str` is "typing" to
* **y**,The y coordinate That the `str` is "typing" to
* **Str**,**It is a String That you wanted to type on Screen, IT NEEDS TO BE LESS THAN 16 CHARACTERS**
 
In The function, Raspberry Pi Will move The cursor To the specific place That you pointed, then it will try to send the character in the string by sending asciis.

## First Try
```python
init_lcd()
print_lcd(0, 0, 'Hello, world!')
```
By using those function, You could see "Hello World" On the first line of the LCD1602
# Combine With HeWeather API
Also, The With the LCD1602 Module, We can combine it with HeWeather API Easily, For register A HeWeather API account Online, You can just Reference Online Resources, and now, I will mainly phase in the Code we got for API calls.
```python
import requests
import pprint
Key = "&key=" + ""          #input keys
CityName = ""
def Getcity(CityName):
    url_v2 = "https://geoapi.qweather.com/v2/city/lookup?location=" + CityName + Key
    CityArg =  requests.get(url_v2).json()['location'][0]
    return CityArg["id"]
    
    
def GetInfo(location):
    url = "https://devapi.qweather.com/v7/weather/now?" + Key + "&location=" + location
    return requests.get(url).json()

def RetWea():
    CityId = Getcity(CityName)
    return GetInfo(CityId)['now']['temp']

if __name__ == '__main__':
    print("It is: " + WeatherNow['now']['temp'] + " degree")
```
as we can see now, we are using `Request` Method in order to get the `HTML` output of the HeWeather's API server. in this Script, you must edit The `Key` and
`CityName` arguements so we can get positive infomations.  
For Furthermore, I Will not Expain more, It is just a simple API Call , I think you are capable of understanding by your self.
# 8x8 Matrix Project
    
![](https://cdn.jsdelivr.net/gh/DDizzzy79/cdn/posts/20211209193815.png)  
   
**Max7219 is a set of LED Which Makes a 8x8 Matrix display screen, it is able to show anything but in a limit space**   
For the Matrix Project, We selected the `Max7219` With the `spi`. You need to Connect the pins like below:   
   
|Name|Function|RPi Function|
|----|--------|------------|
|VCC|5V Connection|5V|
|GND|Ground|0V/GND|
|DIN|Data In|MOSI|
|CS|Chip Select|SPI CE0|
|CLK|Clock|SPI CLK|
    
Firstly, We need to enable the spin method in Raspberry Pi by using `sudo raspi-config`. After configuration, You can use `lsmod | grep -i spi` and `ls -l /dev/spi*` to check the conect with the `MAX7219`, If you had a a Affirmative Responde on the terminal, That means we can move to the next step.  
## Manipulating MAX7219
We can controll MAX7219 By using https://github.com/rm-hull/luma.led_matrix repository. You can install the module by using `python3 -m pip install`,After cloning the repository into your host machine, you can check for the arguement by using `python3 examples/matrix_demo.py -h`.   
   
```shell
$ python3 examples/matrix_demo.py -h
usage: matrix_demo.py [-h] [--cascaded CASCADED]
                      [--block-orientation {0, 90, -90}]

matrix_demo arguments

optional arguments:
-h, --help            show this help message and exit
--cascaded CASCADED, -n CASCADED
                      Number of cascaded MAX7219 LED matrices (default: 1)
--block-orientation {0, 90, -90}
                      Corrects block orientation when wired vertically
                      (default: 0)
```

you can test your `Max7219` by run This Python script. This will display different symbol and character.  
## IOT Connections
If you had read our's iot_controll project carefully, you can find a part of Code which is use to manipulating MAX7219.  
  
```python
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
```
  
As we can see here, We are trying to output a symobols (technically a character.) by using ASCII code. Also, you can try to display any character you wanted by searching  `ASCII chart`.
