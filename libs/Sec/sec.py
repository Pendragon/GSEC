'''
File          : sec.py
Project       : GSEC
Description   : Sec module 
Author        : Jean-Paul GERST

File Created  : Friday, 28th January 2022 9:20:39 pm
Last Modified : Tuesday, 8th February 2022 8:31:54 am

Copyright (c) : 2022 Jean-Paul GERST
'''

import gpiozero

class Sec:
    def __init__(self, config):
        self.config = config
        self.abscent = True
        self.keypad_green = gpiozero.LED(self.config['KEYPAD_GREEN_LED'])
        self.keypad_red = gpiozero.LED(self.config['KEYPAD_RED_LED'])
        self.keypad = gpiozero.Button(self.config['KEYPAD'])
        self.alive = gpiozero.Button(self.config['KEYPAD_ALIVE'])
        self._abscent()

    def _abscent(self):
        # Passage du mode abscent au mode present
        # => L'alarme est inactivé
        if self.abscent == False and self.keypad.is_pressed:
            self.abscent = True
            self.keypad_red.on()
            self.keypad_green.off()
        # Passage du mode present au mode abscent
        # => L'alarme est activée
        elif self.abscent == True and self.keypad.is_pressed == False:
            self.abscent = False
            self.keypad_red.off()
            self.keypad_green.on()

    def update(self):
        self._abscent()

    def shutdown(self):
        self.keypad_red.off()
        self.keypad_green.off()

