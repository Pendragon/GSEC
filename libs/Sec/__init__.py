'''
File          : __init__.py
Project       : GSEC
Description   : Sec module 
Author        : Jean-Paul GERST

File Created  : Thursday, 27th January 2022 9:40:35 pm
Last Modified : Thursday, 27th January 2022 9:57:11 pm

Copyright (c) : 2022 Jean-Paul GERST
'''

import gpiozero
import globals

def setup(config):
    global keypad_green = gpiozero.LED(globals.config.sec.KEYPAD_GREEN_LED)
    global keypad_red = gpiozero.LED(globals.config.sec.KEYPAD_RED_LED)
    global led = gpiozero.LED(globals.sec.LED)
    global keypad = gpiozero.Button(globals.sec)
    
    pass

def update():
    
    pass

def shutdown():
    pass

