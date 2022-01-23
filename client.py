'''
File          : client.py
Project       : GSEC
Description   : 
Author        : Jean-Paul GERST

File Created  : Sunday, 23rd January 2022 5:48:01 pm
Last Modified : Sunday, 23rd January 2022 9:00:12 pm

Copyright (c) : 2022 Jean-Paul GERST
'''

import toml
import logging
import globals

def setup():
    globals.config = toml.load("config.toml")
    logging.info('Booting...')
    logging.info('All systems UP')
    globals.run = True

def loop():
    pass

def shutdown():
    pass

def main():
    try:
        setup()
        while globals.run:
            loop()
    finally:
        shutdown()

if __name__ == "__main__":
    main()
