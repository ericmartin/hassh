#!/usr/bin/env python
'''
Connect via ssh to help generate data for hasshgen
:param hostname: string
'''
import sys
import paramiko

# TODO: trap with if / try except on indexError
hostname = sys.argv[1]
PORT = 22
USR = 'user'
PWD = 'pass'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect(hostname, port=PORT, username=USR, password=PWD)
except paramiko.SSHException as my_error:
    raise
