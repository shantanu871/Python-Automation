'''5. In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. 
Create a Python program that processes this YAML file and then uses Netmiko to connect to the leaf1 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. 
The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.
'''


import yaml
from netmiko import ConnectHandler

with open(".netmiko.yml") as f:
    load_file = yaml.safe_load(f)

leaf1 = load_file["juniper1"]


net_connect = ConnectHandler(**leaf1)

print()
print(net_connect.find_prompt())
print()
'''

below is the outout
(.venv) root@ubuntu:~/Python-Automation/class3# python3 yaml_ex5.py

python@leaf>     <<####this

(.venv) root@ubuntu:~/Python-Automation/class3#
'''
