import mpr121
import time
from machine import Pin, I2C

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
mpr = mpr121.MPR121(i2c)
push_button = Pin(28, Pin.IN, Pin.PULL_DOWN)

btns_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def save_code():
    print('=============')
    print('| {} | {} | {} |'.format(btns_code[0], btns_code[1], btns_code[2]))
    print('| {} | {} | {} |'.format(btns_code[3], btns_code[4], btns_code[5]))
    print('| {} | {} | {} |'.format(btns_code[6], btns_code[7], btns_code[8]))
    print('=============')





while True:
    logic_state = push_button.value()

    if logic_state:
        save_code()

    for i in range(9):
        if mpr.is_touched(i):
            btns_code[i] = 1
            print('Key {} pressed'.format(i))

    time.sleep_ms(100)
