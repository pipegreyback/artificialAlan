# -*- coding: UTF-8 -*-

from . import log

app_name = 'ArtificialAlan'
author = 'Cristóbal Ganter'
author_email = 'cganterh@gmail.com'
debug = True
port = 52002

proxy_scheme = 'https'
proxy_host = 'mem.cganterh.net'
proxy_port = None

#CLIENT SPECIFIC:
ws_scheme = 'wss'
user_scalable_viewport = 'no'    #accepted values are 'yes'
                                 #and 'no'

#SERVER SPECIFIC:
secrets_file = 'secrets.json'
database_name = 'artalan'
short_account_exp = {'minutes': 5}
long_account_exp = {'days': 30 if not debug else 1}
