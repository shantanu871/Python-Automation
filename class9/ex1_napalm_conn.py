"""

1. Simple NAPALM Connections and Facts

1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device. Use getpass() for the password handling. This Python module should be used to store the device connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the my_devices.py file and creates a NAPALM connection object. This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using your "my_devices.py" file and your NAPALM connection function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection object itself. Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).
"""

from napalm import get_network_driver
from pprint import pprint
from my_devices import network_devices

def napalm_connection(dev):
    """Func to open NAPALM
     Platform defined in my_devices is invalid, so we copy to new new variable so  original object is not modified..and we creat new device object in this code that doesnt affect device dict in      my_devices
     """

    device = dev.copy()
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn
"""
Func is part 1b

What does driver(**device) mean?
driver: The class blueprint fetched by get_network_driver(). Adding parentheses (...) turns the blueprint into a real, live instance.

** (Dictionary Unpacking): It does not perform math. Instead, it tells Python: "Take this dictionary, rip open the box, and scatter its keys and values out as individual keyword arguments."

Behind the scenes translation: driver(**device) becomes driver(hostname="...", username="...", password="...").
"""
#Below is 1c

if __name__ == "__main__":
# we need ot create list as asked
    connections = []
    for x in network_devices:
        conn = napalm_connection(x)
        connections.append(conn)

#1d- print connection obj and facts 
for x in connections:
    print("-" *20)
    print(x)
    print("\n" *5)
    print("-" *20)
    pprint(x.get_facts())
    print("*" *20)
    x.close()
print("\n\n")
"""
(.venv) root@ubuntu:~/Python-Automation/class9# python3 ex1_napalm_conn.py
Password:
--------------------
<napalm.junos.junos.JunOSDriver object at 0x7ea09fa03e30>






--------------------
{'fqdn': 'simba.ultralab.juniper.net',
 'hostname': 'simba',
 'interface_list': ['vcp-255/1/0',
                    'vcp-255/1/1',
                    'vcp-255/1/2',
                    'vcp-255/1/3',
                    'ge-0/0/0',
                    'gr-0/0/0',
                    'pfe-0/0/0',
                    'pfh-0/0/0',
                    'ge-0/0/1',
                    'ge-0/0/2',
                    'ge-0/0/3',
                    'ge-0/0/4',
                    'ge-0/0/5',
                    'ge-0/0/6',
                    'ge-0/0/7',
                    'ge-0/0/8',
                    'ge-0/0/9',
                    'ge-0/0/10',
                    'ge-0/0/11',
                    'ge-0/0/12',
                    'ge-0/0/13',
                    'ge-0/0/14',
                    'ge-0/0/15',
                    'ge-0/0/16',
                    'ge-0/0/17',
                    'ge-0/0/18',
                    'ge-0/0/19',
                    'ge-0/0/20',
                    'ge-0/0/21',
                    'ge-0/0/22',
                    'ge-0/0/23',
                    'ge-0/0/24',
                    'ge-0/0/25',
                    'ge-0/0/26',
                    'ge-0/0/27',
                    'ge-0/0/28',
                    'ge-0/0/29',
                    'ge-0/0/30',
                    'ge-0/0/31',
                    'ge-0/0/32',
                    'ge-0/0/33',
                    'ge-0/0/34',
                    'ge-0/0/35',
                    'ge-0/0/36',
                    'ge-0/0/37',
                    'ge-0/0/38',
                    'ge-0/0/39',
                    'ge-0/0/40',
                    'ge-0/0/41',
                    'ge-0/0/42',
                    'ge-0/0/43',
                    'ge-0/0/44',
                    'ge-0/0/45',
                    'ge-0/0/46',
                    'ge-0/0/47',
                    'xe-0/2/0',
                    'xe-0/2/1',
                    'xe-0/2/2',
                    'xe-0/2/3',
                    '.local.',
                    'ae3',
                    'bme0',
                    'dsc',
                    'fti0',
                    'gre',
                    'ipip',
                    'irb',
                    'jsrv',
                    'lo0',
                    'lsi',
                    'me0',
                    'mtun',
                    'pimd',
                    'pime',
                    'tap',
                    'vme'],
 'model': 'EX4300-48P',
 'os_version': '21.4R3-S11.3',
 'serial_number': 'PD3715430598',
 'uptime': 12615198,
 'vendor': 'Juniper'}
********************
"""
