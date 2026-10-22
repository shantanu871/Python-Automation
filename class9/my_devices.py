import os
from getpass import getpass

"""
Dynamic Credentials (os & getpass):

It checks if an environment variable named PYNET_PASSWORD is already set. If it is, it grabs it automatically (great for running scripts without typing passwords every time).

If it isn't set, it falls back to getpass() to securely prompt you for your password in the terminal.
"""

username = "python"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

EX1 = {
        "hostname" : "10.85.173.163",
        "username" : username,
        "password" : password,
        "platform" :"junos",
    }

network_devices = [EX1]
