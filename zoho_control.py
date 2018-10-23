#!/usr/bin/python

import requests
import json

auth_token = 'a5f59766837a1bc0e907cd1f9bdc393f'
org_id ='28909986'
department_id = '41840000000006907'

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


#rs = ZohoWorker(department_id, auth_token, org_id)
#print(str(rs.getTicketsByStatus(Status.pending)))

