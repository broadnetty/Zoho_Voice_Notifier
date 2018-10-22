#!/usr/bin/python

import logging
from logging.config import fileConfig
import datetime
import requests
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
    r = requests.get(
        url='https://accounts.zoho.com/oauth/v2/auth?scope=ZohoCRM.users.ALL&client_id=1000.XP3JWFE5GPR51392180R2L6QAHXEVQ&response_type=code&access_type=online',
        params=None, verify=False)
    print(r.content)


