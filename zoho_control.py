#!/usr/bin/python

import requests



code='1000.13be7bd72011954131cdc31edfbd28ad.f49fb56b6ecf5c167143f552ca49e5d6'
redirect_uri='https://support.n2ws.com/oauthgrant'
client_id='1000.XP3JWFE5GPR51392180R2L6QAHXEVQ'
client_secret='0c04938d2ab34db074b5429d0ef39dea945f9d4ac0'
grant_type='authorization_code'

url='https://accounts.zoho.com/oauth/v2/token?code=' + code + \
    'redirect_uri={}&client_id=' + client_id +\
    '&client_secret=' + client_secret + \
    '&grant_type=' + grant_type

r = requests.get(url='https://accounts.zoho.com/oauth/v2/auth?scope=ZohoCRM.modules.ALL&client_id=1000.13be7bd72011954131cdc31edfbd28ad.f49fb56b6ecf5c167143f552ca49e5d6&response_type=code&access_type=online&redirect_uri=https://support.n2ws.com/oauthgrant',params=None,verify=False)
