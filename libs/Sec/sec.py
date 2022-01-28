'''
File          : sec.py
Project       : GSEC
Description   : Sec module 
Author        : Jean-Paul GERST

File Created  : Friday, 28th January 2022 9:20:39 pm
Last Modified : Friday, 28th January 2022 9:35:12 pm

Copyright (c) : 2022 Jean-Paul GERST
'''

import gpiozero

class Sec:
    def __init__(self, config):
        self.config = config
        self.keypad_green = gpiozero.LED(self.config.KEYPAD_GREEN_LED)
        self.keypad_red = gpiozero.LED(self.config.KEYPAD_RED_LED)
        self.led = gpiozero.LED(self.sec.LED)
        self.keypad = gpiozero.Button(self.config.KEYPAD)
        self._abscent()

    def _abscent(self):
        if self.keypad.is_pressed:            
            self.abscent = True
            self.keypad_red.on()
            self.keypad_green.off()
            self.led.on()
        else:
            self.abscent = False
            self.keypad_red.off()
            self.keypad_green.on()
            self.led.off()

    def update(self):
        self._abscent()

    def shutdown(self):
        self.keypad_red.off()
        self.keypad_green.off()
        self.led.off()

