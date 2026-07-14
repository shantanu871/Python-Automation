'''
1) import device cred from my_devices.py
2) on both devices, SSH and dump the config using template

We re using PyEz

You will never write import pyez in your code.

The software package itself is called PyEZ on the internet, and you install it using pip install junos-eznc. However, inside the actual source code library, the creators chose to name the top-level Python folder jnpr (short for Juniper).
'''

import os
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

'''
ere is exactly what those two specific Juniper PyEZ imports do under the hood:

1. from jnpr.junos import Device
Think of Device as your transport layer engine.

What it does: It sets up the physical network connection to your switch. When you pass it parameters like host, user, and password, it reaches out over the network and opens a secure NETCONF-over-SSH session to the Junos platform.

Analogy: It is the equivalent of opening your terminal, typing ssh python@10.85.173.165, and successfully logging into the box. It manages the connection state machine.

2. from jnpr.junos.utils.config import Config
Think of Config as your configuration database manager.

What it does: Once Device opens the connection channel, Config provides the tools to interact with the Junos configuration database. It gives you the programmatic commands to manipulate the candidate database—specifically methods like .load() (to push the text strings you render) and .commit() (to activate the changes).

Analogy: It is the equivalent of typing configure private at the CLI, typing out your set commands, running a commit check, and typing commit.

Why they are separate:
PyEZ separates them by design. You use Device to manage the connection itself, and you use utility modules like Config only when you need to change configurations. If you just wanted to check interface statuses or check routing tables without changing any configuration, you would import Device, but you wouldn't need to import Config at all!

'''

from my_devices import jnpr1, jnpr2 #this wil import from my_devices.py

if __name__ =="__main__":
    #Setup Jinja Environmrnt
    env = Environment(undefined=StrictUndefined, loader=FileSystemLoader("./templates/exercise2"))
    template_file = "junos_bgp.j2"

    #Define device specific vars

    jnpr1_vars = {"device_name":"Rocket", "interface" : "ge-0/0/26", "ipv4_address" : "10.1.100.1", "ipv4_netmask" : "24", "local_as": "22"}
    jnpr2_vars = {"device_name":"Simba", "interface" : "ge-0/0/26", "ipv4_address" : "10.1.100.2", "ipv4_netmask" : "24", "local_as": "22"}

    # Criss cross peer ip
    jnpr1_vars["peer_ip"] = jnpr2_vars["ipv4_address"]
    jnpr2_vars["peer_ip"] = jnpr1_vars["ipv4_address"]


    #Join Jnpr and jnpr_vars so we can iterate for loop over one nested dict, else we need nested for loop

    jnpr1["j2_vars"] = jnpr1_vars
    jnpr2["j2_vars"] = jnpr2_vars

    print("jnpr1 with j2_vars is")
    print(jnpr1)
    print()
    print("jnpr2 with j2_vars is")
    print()
    print(jnpr2)
    print("#"*80)

#loop over jnpr1 and 2
    for device in (jnpr1, jnpr2):
        j2_vars = device["j2_vars"] # grab j2_vars from 'device'- jnpr1 and 2
        # rendwer template amd pass j2_vars

        template = env.get_template(template_file)
        cfg_text = template.render(**j2_vars)

        #Open NETCONF usig PyEZ
        with Device(host=device["host"], user=device["username"], passwd=device["password"]) as dev:

                    #open config mode
                    with Config(dev) as cu:
                        print(f"Loading config in {j2_vars["device_name"]}")
                        cu.load(cfg_text, format="set")
                    print("performing commit")
                    cu.commit()
                    print(f"Committed config on {j2_vars["device_name"]}")
                    print(f"fetch BGP summary from {j2_vars["device_name"]}")
                    print("*" *50)
                    bgp_summary = dev.cli(" show bgp summary")
                    print(bgp_summary)
                    print("*" *50)


                    '''
                    (.venv) root@ubuntu:~/Python-Automation/class5# python3 exercise2c.py
jnpr1 with j2_vars is
{'host': '10.85.173.165', 'username': 'python', 'password': 'Python', 'j2_vars': {'device_name': 'Rocket', 'interface': 'ge-0/0/26', 'ipv4_address': '10.1.100.1', 'ipv4_netmask': '24', 'local_as': '22', 'peer_ip': '10.1.100.2'}}

jnpr2 with j2_vars is

{'host': '10.85.173.163', 'username': 'python', 'password': 'Python', 'j2_vars': {'device_name': 'Simba', 'interface': 'ge-0/0/26', 'ipv4_address': '10.1.100.2', 'ipv4_netmask': '24', 'local_as': '22', 'peer_ip': '10.1.100.1'}}
################################################################################
Loading config in Rocket
performing commit
Committed config on Rocket
fetch BGP summary from Rocket
**************************************************
/root/Python-Automation/.venv/lib/python3.12/site-packages/jnpr/junos/device.py:729: RuntimeWarning:
CLI command is for debug use only!
Instead of:
cli(' show bgp summary')
Use:
rpc.get_bgp_summary_information()

  warnings.warn(warning_string, RuntimeWarning)

Threading mode: BGP I/O
Default eBGP mode: advertise - accept, receive - accept
Groups: 2 Peers: 2 Down peers: 1
Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
inet.0
                       0          0          0          0          0          0
Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
10.1.100.2               22          0          0       0       0           2 Active
10.64.51.65           22773     538444     539018       0    1016 3w1d 11:13:08 Establ
  inet.0: 0/0/0/0

**************************************************
Loading config in Simba
performing commit
Committed config on Simba
fetch BGP summary from Simba
**************************************************
/root/Python-Automation/.venv/lib/python3.12/site-packages/jnpr/junos/device.py:729: RuntimeWarning:
CLI command is for debug use only!
Instead of:
cli(' show bgp summary')
Use:
rpc.get_bgp_summary_information()

  warnings.warn(warning_string, RuntimeWarning)

Threading mode: BGP I/O
Default eBGP mode: advertise - accept, receive - accept
Groups: 1 Peers: 1 Down peers: 1
Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
inet.0
                       0          0          0          0          0          0
Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
10.1.100.1               22          0          0       0       0           2 Active

**************************************************
'''

