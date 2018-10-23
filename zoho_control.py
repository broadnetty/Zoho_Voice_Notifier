#!/usr/bin/python

import requests
import json

auth_token='Zoho-authtoken a5f59766837a1bc0e907cd1f9bdc393f'
org_id ='28909986'
code='1000.13be7bd72011954131cdc31edfbd28ad.f49fb56b6ecf5c167143f552ca49e5d6'
redirect_uri='https://support.n2ws.com/oauthgrant'
client_id='1000.XP3JWFE5GPR51392180R2L6QAHXEVQ'
client_secret='0c04938d2ab34db074b5429d0ef39dea945f9d4ac0'
grant_type='authorization_code'

url=' https://desk.zoho.com/api/v1/ticketsByStatus?departmentId=41840000000006907&status=Waiting for the customer&include=contacts,assignee'

HEADERS = { 'Authorization' : auth_token, 'orgId' : org_id}

r = requests.get(url=url, headers=HEADERS)

print(r.content)

response = json.loads(r.content)

with open('tempsubj.txt', 'w') as out:
    for ticket in response['data']:
        print(ticket['subject'])
        out.write(ticket['subject'] + '. Next case: ')