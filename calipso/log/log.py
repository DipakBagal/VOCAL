###################################
#   Created on June 29, 2015
#
#   @authors: Grant Mercer, Nathan Qian
###################################
import logging.config
import sys
import os
import traceback
from constants import PATH

config = {
          'version': 1,
          'disable_existing_loggers': False,
          'formatters': {
                'logfileformatter': {
                    'format': '[%(asctime)s] [%(levelname)8s] --- %(message)s... (%(filename)s:%(lineno)s)'
                    },
                },
          'handlers': {
                'logfile': {
                    'class': 'logging.FileHandler',
                    'level': 'NOTSET',
                    'filename': PATH + '/log/trace.log',
                    'mode': 'w+',
                    'formatter': 'logfileformatter'
                    },
                'consoleHandler': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'logfileformatter',
                    'level': 'NOTSET',
                    'stream': 'ext://sys.stdout'}
                },
          'loggers': {
                '': {
                     'handlers': ['logfile', 'consoleHandler'],
                     'level': 'DEBUG',
                     'propagate': True
                     }
                }
          }

def uncaught_exception(exctype, value, tb):
    logging.exception('{0}: {1}'.format(exctype, value))    #kdm
    #logger.exception("Uncaught exception: {0}".format(str(value)))
    #sys.__excepthook__(exctype, value, tb)
    logging.exception(''.join(traceback.format_tb(tb)))    #kdm


sys.excepthook = uncaught_exception
# logging.config.fileConfig(r'/home/gdev/Github/vocal/calipso/log/logging.ini',
# disable_existing_loggers=False)
logger = logging.getLogger('VOCAL')

logging.config.dictConfig(config)

if __name__ == '__main__':
    pass
