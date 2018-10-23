#!/usr/bin/python

import requests
import json

data = { 'auth_token':'a5f59766837a1bc0e907cd1f9bdc393f', 'org_id' : '28909986', 'department_id' : '41840000000006907' }

class Status:
    pending = 'Waiting for the customer'
    open = 'Open'
    hold = 'On hold'
    closed = 'Closed'

class ZohoWorker:

    def __init__(self, config_data):
        self.department_id = config_data['department_id']
        self.auth_token_id = config_data['auth_token']
        self.org_id = config_data['org_id']
        self.HEADERS = {'Authorization': str('Zoho-authtoken ' + self.auth_token_id), 'orgId': self.org_id}
        return

    def getTicketsByStatus(self, status):
        url = 'https://desk.zoho.com/api/v1/ticketsByStatus?departmentId=41840000000006907&status=' \
                   + status
                   #+ '&include=contacts,assignee'
        return self.APIrequest(url)

    def APIrequest(self,r_url):
        r = requests.get(url=r_url, headers=self.HEADERS)
        response = json.loads(r.content)
        return response['data']


#rs = ZohoWorker(data)
#print(str(rs.getTicketsByStatus(Status.pending)))

# {
# 	'id': '41840000014331385',
# 	'ticketNumber': '6936',
# 	'email': 'karthik.e@tgbl.com',
# 	'phone': None,
# 	'subject': 'Backup Snapshots not getting cleaned up after retention',
# 	'status': 'Waiting for the customer',
# 	'statusType': 'Open',
# 	'createdTime': '2018-08-02T03:59:15.000Z',
# 	'category': None,
# 	'subCategory': None,
# 	'priority': 'High',
# 	'channel': 'Web',
# 	'dueDate': '2018-08-02T09:59:15.000Z',
# 	'responseDueDate': None,
# 	'commentCount': '0',
# 	'threadCount': '8',
# 	'closedTime': None,
# 	'departmentId': '41840000000006907',
# 	'contactId': '41840000013296001',
# 	'productId': '41840000000038315',
# 	'assigneeId': '41840000011926067',
# 	'teamId': None,
# 	'webUrl': 'https://support.n2ws.com/support/n2wsoftware/ShowHomePage.do#Cases/dv/7bd1b782e1ba73958e9f8c6fb72e549fe612657a51fd5fbe',
# 	'customerResponseTime': '2018-08-02T08:31:53.000Z',
# 	'lastThread': {
# 		'channel': 'EMAIL',
# 		'isDraft': False,
# 		'isForward': False,
# 		'direction': 'out'
# 	}
# }