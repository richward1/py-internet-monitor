"""
Ping

Simple method to carry out a single ping of the specified hostname.
Returns true if successful.
"""

import platform
import subprocess
import os

def ping(hostname):

    #if Windows, use '-n'
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', hostname]

    # Returns bool
    return subprocess.call(command, stdout=open(os.devnull, 'wb')) == 0