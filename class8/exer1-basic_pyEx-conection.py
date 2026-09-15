#1. PyEZ basic connection and facts:

#1a. Create a PyEZ Device object from the jnpr.junos Device class.
# This device object should connect to "srx2.lasthop.io". Use getpass() 
#to enter the device's password.
# Pretty print all of the device's facts. Additionally, retrieve and print
#only the "hostname" fact.

import os
from getpass import getpass
from pprint import pprint
from jnpr.junos import Device

"""
Python
import os
What it does: Imports Pythons built-in os module, which provides a way to interact with the underlying operating system running your script.

Why its used here: In production PyEZ scripts, os is typically used to handle environment variables or directory paths safely. For instance, rather than hardcoding credentials into your script, you can use os.environ.get("JUNOS_PASSWORD") or locate SSH key files stored on your machine.

Python
from getpass import getpass
What it does: Imports the getpass() function from Pythons standard library.

Why its used here: It prompts the user for a password in the terminal without echoing back characters to the screen. This keeps passwords from displaying in plain text on your console or showing up in terminal log history.

Python
from pprint import pprint
What it does: Imports the "pretty-print" function (pprint) from Pythons pprint module.

Why its used here: Standard print() outputs complex data structures (like large dictionaries or lists of facts) as a single, messy wall of text. pprint() automatically indents, formats, and breaks those nested data structures across multiple lines so they are easy to read.

Python
from jnpr.junos import Device
What it does: Imports the core Device class directly from Junipers PyEZ framework (jnpr.junos).

Why its used here: Device is the fundamental building block of PyEZ. It represents the physical or virtual Juniper switch/router and handles authentication, establishing the NETCONF-over-SSH session, executing RPC calls (dev.rpc), gathering system facts (dev.facts), and closing sessions cleanly.
"""

password=os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

#create Pyez Device object

my_dev = Device(host = "10.85.173.163", user = "python", passwd = password )

#create Netconf session-

my_dev.open()

print()
print("Print dev facts")
print("-" *20)
pprint(my_dev.facts)

print("\n\n")
print("print hostname from device facts")
print("-" *20)
print(my_dev.facts["hostname"])
print()
#if you also want prompt for uname- username = os.getenv("PYNET_USER") if os.getenv("PYNET_USER") else input("Enter username: ")
"""
(.venv) root@ubuntu:~/Python-Automation/class8# python3 exer1-basic_pyEx-conection.py
Password:

Print dev facts
--------------------
{'2RE': False,
 'HOME': '/var/home/python',
 'RE0': {'last_reboot_reason': '0x1:power cycle/failure',
         'mastership_state': 'master',
         'model': 'EX4300-48P',
         'status': 'OK',
         'up_time': '17 days, 5 hours, 32 minutes, 15 seconds'},
 'RE1': None,
 'RE_hw_mi': False,
 'current_re': ['master',
                'node',
                'fwdd',
                'member',
                'pfem',
                're0',
                'fpc0',
                'localre'],
 'domain': 'ultralab.juniper.net',
 'fqdn': 'simba.ultralab.juniper.net',
 'hostname': 'simba',
 'hostname_info': {'fpc0': 'simba'},
 'ifd_style': 'SWITCH',
 'jnu_satellite': False,
 'junos_info': {'fpc0': {'object': junos.version_info(major=(21, 4), type=R, minor=3-S11, build=3),
                         'text': '21.4R3-S11.3'}},
 'master': 'RE0',
 'model': 'EX4300-48P',
 'model_info': {'fpc0': 'EX4300-48P'},
 'personality': 'SWITCH',
 're_info': {'default': {'0': {'last_reboot_reason': '0x1:power cycle/failure',
                               'mastership_state': 'master',
                               'model': 'EX4300-48P',
                               'status': 'OK'},
                         'default': {'last_reboot_reason': '0x1:power '
                                                           'cycle/failure',
                                     'mastership_state': 'master',
                                     'model': 'EX4300-48P',
                                     'status': 'OK'}}},
 're_master': {'default': '0'},
 'satellites_info': {},
 'serialnumber': 'PD3715430598',
 'srx_cluster': None,
 'srx_cluster_id': None,
 'srx_cluster_redundancy_group': None,
 'switch_style': 'VLAN_L2NG',
 'vc_capable': True,
 'vc_fabric': False,
 'vc_master': '0',
 'vc_mode': 'Enabled',
 'version': '21.4R3-S11.3',
 'version_RE0': None,
 'version_RE1': None,
 'version_info': junos.version_info(major=(21, 4), type=R, minor=3-S11, build=3),
 'virtual': False,
 'vmhost': False,
 'vmhost_info': {}}



print hostname from device facts
--------------------
simba
"""
