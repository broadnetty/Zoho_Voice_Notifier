#!/usr/bin/python

import logging
from logging.config import fileConfig
import datetime
import os, platform

def init():
    #logger init
    #fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logging.basicConfig(filename='logs\\' + str(datetime.datetime.today()).replace(':','-') + '.log',
                        filemode='a',
                        level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    logging.debug("Process exited %s", "successfully")
    return logger

if __name__ == '__main__':
    logger = init()
