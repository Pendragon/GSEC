import logging
import coloredlogs

__author__  = "Vinay Sajip <vinay_sajip@red-dove.com>"
__status__  = "production"
# The following module attributes are no longer updated.
__version__ = "0.5.1.2"
__date__    = "07 February 2010"

__all__ = ['log']

level = logging.DEBUG
log = logging.getLogger(__name__)

fieldstyle = {'asctime': {'color': 'green'},
            'levelname': {'bold': True, 'color': 'black'},
            'filename':{'color':'cyan'},
            'funcName':{'color':'blue'}}
                                    
levelstyles = {'critical': {'bold': True, 'color': 'red'},
            'debug': {'color': 'green'}, 
            'error': {'color': 'red'}, 
            'info': {'color':'magenta'},
            'warning': {'color': 'yellow'}}

coloredlogs.install(level,
                    logger=log,
                    fmt='%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s',
                    datefmt='%H:%M:%S',
                    field_styles=fieldstyle,
                    level_styles=levelstyles)

file = logging.FileHandler("logs\latest.log")
fileformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file.setLevel(level)
file.setFormatter(fileformat)

log.addHandler(file)

def info(param):
    log.info(param)

def debug(param):
    log.debug(param)

def warning(param):
    log.warning(param)

def error(param):
    log.error(param)

