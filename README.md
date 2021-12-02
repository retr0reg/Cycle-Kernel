# Cyclic 's Kernel ![](https://img.shields.io/badge/SupportedBy-Ret1w1cky-blueviolet)
![ead16cbfc626e7ad4fa6ea3a64bf853](https://user-images.githubusercontent.com/72267897/144238466-848c703b-9984-4fad-a44a-e673dd136799.jpg)  
---- **A iot Bike sytem based on RaspberryPi, Ardiuino, etc**  
## 0x1 What is This?
Cyclic 's Kernel is an independent System With self-producing energy iot Web control, The system 's Energy Source is a 12V6W Generater. And The Voltage, Current is not cocerned, Now, I will introduce those stuff to You
[Plan.pdf](https://github.com/DDizzzy79/ScienceFair/files/7633868/default.pdf)  
Also, for a extra info, Lots of our code is based on lots of thoughts on internet
## 0x2 Basic plans
Our plan inclues that:  
* Generater
* Clock(Shows Velocity&Time)
* Controled turning light
* Energy Store Device
* Other IOT Devices
# Generaters
For our Generaters, We selected A **12V6WGenerater** , So Far, The maximum of it is aboat ``5~6V``  
But, We were not exclude That the generater can generate above 6V, So far, The generater 's voltage output had exceed our's minimum request.  
We chose to install it on the wire of the tire It work pretty well, We can get 5~6v during a normal ride.
# RaspberryPi
![image](https://user-images.githubusercontent.com/72267897/144403737-64037c69-4959-492a-bb5d-5c7ec4068d5b.png)  
For ours SBC (single-board Computer) We select Raspberry Pi due to the high-functing & the Raspberry-based environment, I found a RaspberryPi 4B, By using Serial Port debugging, I sucessfuly install Respberry Linux kernel ,After Then, it was a boring time of debugging & installing....... Environment. Anyway We First tried to to a basic IO In/Out Circius by coding a Python script With RPi.GIPO, also be carful when setting the IO port for BMC   
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
This script will First, it will set the pin finding mode to ``bmc``,thenit will set the p (GPIO.11) pin to output mode, After That, Raspberry Pi is going to run the scrpit in the `while loop` Which is set the `p` to high, Wait for 1 seconds set the `p` to low. repeated and repeated.  
btw, You can The IO pin setting by using ``gpio readall``  
```
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
