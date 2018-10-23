#!/usr/bin/python

import logging
from google_voice_API import *
from zoho_control import *

import datetime

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

#if __name__ == '__main__':
#    logger = init()

#rs = ZohoWorker()

config_path="config.json"
#checking for alternate config path
if 'ZOHO_SPEAKER_CONFIG_PATH' in os.environ:
    config_path = os.environ['ZOHO_SPEAKER_CONFIG_PATH']

with open(config_path) as fileconf:
    config = json.load(fileconf)

zoj = ZohoWorker(config['config']['zoho'])
print(zoj.getTicketsByStatus(Status.pending))


