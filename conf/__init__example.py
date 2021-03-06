# -*- coding: UTF-8 -*-

""".. todo:: Describe secret files origin and format."""

from os import environ, path

from urllib.parse import urlunparse

from . import log  # noqa

app_name = 'EduRT'
app_logo_path = './art/favicon/2logo.png'
author = 'Cristóbal Ganter'
author_email = 'cganterh@gmail.com'
login_path = 'signin'

# TORNADO
autoreload = False
debug = True
port = print(
    '### Change port in conf/__init__.py! ###') or 8000

proxy_scheme = 'http'
proxy_host = print(
    '### Change proxy_host in conf/__init__.py! ###') or \
    'localhost'
proxy_port = print(
    '### Change proxy_port in conf/__init__.py! ###') or \
    port
"""Should be ``int`` or None. This is the port you use to
connect from the outside."""

_netloc = proxy_host + (':' + str(proxy_port)
                        if proxy_port else '')
proxy_url = urlunparse(
    (proxy_scheme, _netloc, '', '', '', '')
)

# CLIENT SPECIFIC:
ws_scheme = 'ws'

ws_reconnect_interval = 55
"""In seconds. See
`<https://github.com/joewalnes/reconnecting-websocket
#reconnectinterval>`_."""

user_scalable_viewport = 'no'
"""Accepted values are ``'yes'`` and ``'no'``."""

# SERVER SPECIFIC:
root_path = environ.get('AA_PATH', '')

secrets_file = path.join(
    root_path,
    print(
        '### Change secrets_file in conf/__init__.py! ###')
    or 'secrets/secrets.json'
)

google_secrets_file = path.join(
    root_path,
    print(
        '### Change google_secrets_file in '
        'conf/__init__.py! ###')
    or 'secrets/client_secret_googleCodeThingy1234'
    '.apps.googleusercontent.com.json'
)

ping_sleep = 10
"""In seconds. See :meth:`~controller.MSGHandler.on_pong`"""

ping_timeout = 20
"""In seconds. See :meth:`~controller.MSGHandler.on_pong`"""

database_name = 'artalan'
short_account_exp = {'minutes': 5}
long_account_exp = {'days': 30 if not debug else 1}
