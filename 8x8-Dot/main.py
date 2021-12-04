from luma.led_matrix.device import *
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
import time

def init_max719():
    global serial
    global device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1 or 1, block_orientation=0,rotate=0 or 0, blocks_arranged_in_reverse_order=False)
    print("Initializing.....")
    
def left():
    for x in range(10):
        #print("drawing")
        for x in range(5):
            with canvas(device) as draw:
                text(draw, (0, 0), chr(27), fill="white")
                time.sleep(0.01)
    return 0

def right():
    for x in range(10):
        #print("drawing")
        for x in range(4):
            with canvas(device) as draw:
                text(draw, (0, 0), chr(26), fill="white")
                time.sleep(0.01)
    return 0

if __name__ == '__main__':
    init_max719()
    time.sleep(2)
    left()
    print("turning left")
    right()
    print("turning right")