'''
File          : client.py
Project       : GSEC
Description   : 
Author        : Jean-Paul GERST

File Created  : Sunday, 23rd January 2022 5:48:01 pm
Last Modified : Friday, 28th January 2022 9:36:49 pm

Copyright (c) : 2022 Jean-Paul GERST
'''

import toml
import globals
import traceback

import libs.Log as log
import libs.Sec as sec

def setup():
    globals.config = toml.load("config.toml")
    log.info('Booting...')
    log.info('All systems UP')
    globals.run = True
    sec.setup(globals.config.sec)

def loop():
    sec.update()

def shutdown():
    log.info('Shutting down')
    sec.shutdown()

def main():
    try:
        setup()
        while globals.run:
            loop()
    except:        
        log.error(traceback.format_exc())    
    finally:
        shutdown()

if __name__ == "__main__":
    main()
