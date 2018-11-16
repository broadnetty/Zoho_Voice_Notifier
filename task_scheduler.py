#!/usr/bin/python

import logging
from google_voice_API import *
from zoho_control import *
import msvcrt
import datetime
from datetime import timedelta


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

def kbfunc():
    return msvcrt.getch() if msvcrt.kbhit() else 0

class Task:

    def  __init__(self, func, period):
        self.id = ''
        self.name = 'Task'
        self.start_time = datetime.datetime.now()
        self.period_sec = period
        self.do = self.set_action(func)
        return

    def update(self):
        self.start_time += datetime.timedelta(seconds=self.period_sec)
        return

    def set_action(self,func):
        def wraper():
            func()
            self.update()
        return wraper

class TaskScheduler:

    def __init__(self):
        self.list = list()
        return

    def start_tasks(self):
        while True:
            for task in self.list:
                if task.start_time < datetime.datetime.now() - datetime.timedelta(seconds=task.period_sec):
                    task.do()

    def add_task(self, func, period):
        self.list.append(Task(func, period))
        return


config_path="config.json"

#checking for alternate config path
if 'ZOHO_SPEAKER_CONFIG_PATH' in os.environ:
    config_path = os.environ['ZOHO_SPEAKER_CONFIG_PATH']

with open(config_path) as fileconf:
    config = json.load(fileconf)

zoj = ZohoWorker(config['config']['zoho'])

global_notication = list ()
notificated = list()

def f1():
    for ticket in zoj.getTicketsByStatus(Status.open):
        if ticket['id'] not in notificated:
            global_notication.append(ticket)
            print(datetime.datetime.now())
            print(ticket['ticketNumber'] + ' has added to notified\n')

def f2():
    speaker = SynthSpeaker()
    for item in global_notication:
        if item['id'] not in notificated:
            notificated.append(item['id'])
            text = 'You\'ve got a new open case number ' \
            + item['ticketNumber'] \
            + '. Subject. ' \
            + item['subject']
            speaker.say(text)

def mf1():
    f1()
    f2()

sch = TaskScheduler()
sch.add_task(mf1,5)

print('starting')
sch.start_tasks()

