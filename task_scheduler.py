#!/usr/bin/python

import logging
from google_voice_API import *
from zoho_control import *
import msvcrt
import datetime
from datetime import timedelta

global_slots = 1

def init_loger():
    #logger init
    #fileConfig('logging_config.ini')
    logger = logging.getLogger()
    filename = 'logs\\' + str(datetime.datetime.today()).replace(':','-') + '.log'
    logging.basicConfig(filename=filename,
                        filemode='a',
                        level=logging.INFO,
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    with open('logs\\' + str(datetime.datetime.today()).replace(':','-') + '.log', 'a') as logfile:
        logfile.writelines(['=' * 50,'\nStarting a new log...'])


    return logger


def kbfunc():
    return msvcrt.getch() if msvcrt.kbhit() else 0


#general class for a task. Methods could be overwritten
class Task:

    def __init__(self,task, period):
        self.id = ''
        self.name = 'Task'
        self.next_start_time = datetime.datetime.now()
        self.period_sec = period
        self.do = self.set_action(task.do)
        return

    #should be overloaded
    def setup(self):
        return

    def update_time(self):
        self.next_start_time += datetime.timedelta(seconds=self.period_sec)
        return

    def set_action(self,func):
        def wraper():
            func()
            self.update_time()
        return wraper

#defines the task scheduler. It's better to have one only
class TaskScheduler:

    def __init__(self):
        self.list = list()
        return

    #starts added tasks sequentially (checks if next run time reached then task->do )
    def start_tasks(self):
        while True:
            for task in self.list:
                if task.next_start_time < datetime.datetime.now() - datetime.timedelta(seconds=task.period_sec):
                    task.do()

    def add_task(self, task,period):
        self.list.append(Task(task,period))
        return


class ZHNotifier():
    global_notication = list()
    notificated = list()

    def __init__(self):
        self.config_path = "config.json"
        # checking for alternate config path
        if 'ZOHO_SPEAKER_CONFIG_PATH' in os.environ:
            self.config_path = os.environ['ZOHO_SPEAKER_CONFIG_PATH']

        with open(self.config_path) as fileconf:
            config = json.load(fileconf)

        self.zhworker = ZohoWorker(config['config']['zoho'])
        self.global_tickets_num = int(input("Please input number of tickets you want to pickup (auto): "))
        #tck = self.zhworker.getTicket('41840000017635160') Unassigned
        #tck['status'] = 'Open'
        #print(self.zhworker.patchTicket(tck,'41840000017635160'))

    def get_tickets(self):
        open_tickets = self.zhworker.getTicketsByStatus(Status.open)
        print(str(open_tickets))
        if open_tickets != []:
            for ticket in self.global_notication:
                if ticket not in open_tickets:
                    self.global_notication.remove(ticket)
            for ticket in open_tickets:
                if ticket['id'] not in self.notificated:
                    self.global_notication.append(ticket)
                    print(datetime.datetime.now())
                    print(ticket['ticketNumber'] + ' has added to notified\n')
                    if ticket['assigneeId'] == None and self.global_tickets_num > 0:
                        self.global_tickets_num -= 1
                        print(ticket['ticketNumber'] + " is assigned to you")
                        print("It was in state: "+ticket['status'])
                        speaker = SynthSpeaker()
                        speaker.say('New case assigned to you. Case number ' + ticket['ticketNumber'])
                        tck = self.zhworker.patchTicket({'assigneeId':'41840000015862001'},ticket['id'])



            open_tickets_id = [ ticket['id'] for ticket in open_tickets]
            print("Slots Left: "+str(self.global_tickets_num))

            for ticket_id in self.notificated:
                if ticket_id != None:
                    if ticket_id not in open_tickets_id:
                        try:
                            self.notificated.remove(ticket_id)
                        except Exception as err:
                            print(err)
        else: self.notoficated = []

    def notify(self):
        speaker = SynthSpeaker()
        for item in self.global_notication:
            if item['id'] not in self.notificated:
                self.notificated.append(item['id'])
                text = 'Dear lovely grizzly bear! You\'ve got a new open case number ' \
                + item['ticketNumber'] \
                + '. Subject. ' \
                + item['subject']
                speaker.say(text)

    def pickup(self, id):
        return

    def do(self):
        self.get_tickets()
        self.notify()

def main():
    speaker = SynthSpeaker()
    speaker.say('  Attention! Staying late at the office may harm to your health. Please, finish your tasks as soon as possible and go home. For sake of your own safety, please finish your tasks and go home')
    log = init_loger()
    log.info('Starting new loop')

    sch = TaskScheduler()
    sch.add_task(ZHNotifier(),10)

    print('starting')
    sch.start_tasks()

main()
