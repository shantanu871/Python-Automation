"""
2a. Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2".
This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection.
You should use getpass() for the password handling. You should import this "srx2" device definition for all of the remaining exercises in class8.
"""
import os
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint

username = "python"

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

#Dict for EX (srx)

EX2 = {"host":"10.85.173.163", "user": username, "password": password }
# create a list

junos_devices = [EX2]

