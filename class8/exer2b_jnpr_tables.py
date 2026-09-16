"""

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.


"""
from pprint import pprint
import sys

from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

from exer2a_jnpr_devices import EX2



def check_connected(my_dev):
    print("\n\n")
    if my_dev.connected:
        print(f"Device {my_dev.hostname} is connected")
    else:
        print("failed to connect")
        sys.exit(1)

    
def gather_routes(device):
    routes_table = RouteTable(device)
    routes_table.get()
    return routes_table

def gather_arp_table(device):
    arp_table = ArpTable(device)
    arp_table.get()
    return arp_table


def print_output(dev,routes,arp):
    print()
    print("Print desired output")
    print("-" *20)
    #creating a dict as we need to store data in somethign to print
    devices = {}
    devices["hostname"] = dev.hostname
    devices ["port"] = dev.port
    devices["username"] = dev.user
    # above - user, hostname etc are all attributes..
    devices["route_table"] = routes.items()
    devices["arp_table"] = arp.items()
    pprint(devices)
    print()

"""
The function - for ARP as an eg.- returns an instance of the jnpr.junos.op.arp.ArpTable class, which is a PyEZ Table View object.

Architecturally, this object is a custom dictionary-like wrapper around the XML payload retrieved from Junos over NETCONF.

"""

"""
device["connected_user"] = dev.user
dev.user (Attribute): When you instantiated Device(**srx2), you supplied "user": "python". PyEZ saved that username string to the .user attribute on the Device object.

Dictionary Assignment: This line creates a new key "connected_user" in your local device dictionary and assigns it the string value 'python'.

2. device["route_table"] = routes.items()
routes (PyEZ RouteTable View): In main, routes = gather_routes(device) returned a RouteTable view object that holds all retrieved routes from the switch.

routes.items() (Method Call): Calling .items() converts that RouteTable object into a sequence of key-value tuples representing each prefix and its detailed route entry:

"""

if __name__ == "__main__":
    my_dev = Device(**EX2) #creating an object of class type Device in the exer2a-knpr_devices.py file
    my_dev.open()
    check_connected(my_dev)
    routes = gather_routes(my_dev)
    arp = gather_arp_table(my_dev)

    print_output(my_dev, routes, arp)
"""
When you create the object, PyEZ initializes the Python class instance in memory and stores your parameters (host, user, passwd, etc.). No network traffic happens here.

Step 2: Session Opening (device.open())
When you call device.open(), PyEZ initiates the NETCONF-over-SSH session to the network switch. Once the connection is authenticated, PyEZ automatically runs background operational RPCs to gather system information.

It populates an internal dictionary attribute on the object named device.facts. This dictionary contains retrieved details such as:

hostname

version (Junos OS version)

model (e.g., EX4300)

serialnumber

Step 3: Accessing device.hostname or dev.hostname
hostname is a Python property on the Device class. Under the hood, accessing device.hostname executes a getter method that reads directly from device.facts['hostname']:
"""
"""
(.venv) root@ubuntu:~/Python-Automation/class8# python3 exer2b_jnpr_tables.py
Password:



Device 10.85.173.163 is connected

Print desired output
--------------------
{'arp_table': [('00:00:5e:00:01:06',
                [('mac_address', '00:00:5e:00:01:06'),
                 ('ip_address', '10.85.173.129'),
                 ('interface_name', 'me0.0')]),
               ('d8:b1:22:0a:6e:00',
                [('mac_address', 'd8:b1:22:0a:6e:00'),
                 ('ip_address', '10.85.173.130'),
                 ('interface_name', 'me0.0')]),
               ('0c:86:10:7b:a2:00',
                [('mac_address', '0c:86:10:7b:a2:00'),
                 ('ip_address', '10.85.173.131'),
                 ('interface_name', 'me0.0')]),
               ('20:d8:0b:04:5a:00',
                [('mac_address', '20:d8:0b:04:5a:00'),
                 ('ip_address', '10.85.173.172'),
                 ('interface_name', 'me0.0')]),
               ('00:a0:a5:7c:8c:a3',
                [('mac_address', '00:a0:a5:7c:8c:a3'),
                 ('ip_address', '10.85.173.194'),
                 ('interface_name', 'me0.0')]),
               ('00:a0:a5:72:0d:8e',
                [('mac_address', '00:a0:a5:72:0d:8e'),
                 ('ip_address', '10.85.173.195'),
                 ('interface_name', 'me0.0')]),
               ('e4:5d:37:29:c2:80',
                [('mac_address', 'e4:5d:37:29:c2:80'),
                 ('ip_address', '10.85.173.219'),
                 ('interface_name', 'me0.0')]),
               ('1c:9c:8c:da:65:00',
                [('mac_address', '1c:9c:8c:da:65:00'),
                 ('ip_address', '10.85.173.227'),
                 ('interface_name', 'me0.0')]),
               ('1c:9c:8c:d9:35:00',
                [('mac_address', '1c:9c:8c:d9:35:00'),
                 ('ip_address', '10.85.173.228'),
                 ('interface_name', 'me0.0')]),
               ('1c:9c:8c:da:b5:00',
                [('mac_address', '1c:9c:8c:da:b5:00'),
                 ('ip_address', '10.85.173.233'),
                 ('interface_name', 'me0.0')]),
               ('1c:9c:8c:da:25:00',
                [('mac_address', '1c:9c:8c:da:25:00'),
                 ('ip_address', '10.85.173.234'),
                 ('interface_name', 'me0.0')])],
 'hostname': '10.85.173.163',
 'port': 830,
 'route_table': [('0.0.0.0/0',
                  [('protocol', 'Static'),
                   ('via', 'me0.0'),
                   ('age', 9525302),
                   ('nexthop', '10.85.173.129')]),
                 ('10.1.100.2/32',
                  [('protocol', 'Local'),
                   ('via', None),
                   ('age', 1604982),
                   ('nexthop', None)]),
                 ('10.8.221.5/32',
                  [('protocol', 'Local'),
                   ('via', None),
                   ('age', 8632386),
                   ('nexthop', None)]),
                 ('10.64.101.33/32',
                  [('protocol', 'Local'),
                   ('via', None),
                   ('age', 1392694),
                   ('nexthop', None)]),
                 ('10.85.173.128/25',
                  [('protocol', 'Direct'),
                   ('via', 'me0.0'),
                   ('age', 9525302),
                   ('nexthop', None)]),
                 ('10.85.173.163/32',
                  [('protocol', 'Local'),
                   ('via', 'me0.0'),
                   ('age', 9525302),
                   ('nexthop', None)]),
                 ('ff02::2/128',
                  [('protocol', 'INET6'),
                   ('via', None),
                   ('age', 9525554),
                   ('nexthop', None)])],
 'username': 'python'}



 RT (and ARP) It is a list of tuples, where each tuple contains a string key and a list of key-value tuples.

Here is the exact data hierarchy of route_table:
    # Level 1: Outer Container (List)
[
    # Level 2: Outer Tuple (Key, Value List)
    (
        '0.0.0.0/0',  # Index 0: Prefix String

        # Index 1: Value Container (List of Key-Value Tuples)
        [
            ('protocol', 'Static'),
            ('via', 'me0.0'),
            ('age', 9525302),
            ('nexthop', '10.85.173.129')
        ]
    ),

    (
        '10.1.100.2/32',
        [
            ('protocol', 'Local'),
            ('via', None),
            ('age', 1604982),
            ('nexthop', None)
        ]
    )
]
"""
