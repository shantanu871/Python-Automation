'''
4. You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program. Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses.
Print this dictionary to standard output.
'''

import json
from pprint import pprint

with open("arista_arp.json") as f:
    arp_data = json.load(f)

arp_dict ={}

arp_item = arp_data["ipV4Neighbors"]
for entry in arp_item:
    ip_addr =entry["address"]
    mac_addr =entry["hwAddress"]
    arp_dict[ip_addr]=mac_addr
    
print()
pprint(arp_dict)
print()
print(arp_dict)



'''
The reason .items() was not used in this Arista ARP exercise comes down to a fundamental change in the data structure layout. In the previous NX-OS exercise, we were parsing a nested Dictionary. In this Arista exercise, we are parsing a List of Dictionaries.

Let’s look at the mechanical reason why .items() would actually cause this script to crash.

The Structural Shift: Dict vs. List
Look at what the variable arp_entries actually points to after you extract "ipV4Neighbors":

Python
arp_entries = arp_data["ipV4Neighbors"]
If you look at the JSON file, "ipV4Neighbors" starts with a square bracket [. That means arp_entries is a Python List, not a dictionary:

Python
arp_entries = [
    {"hwAddress": "dc38.e111.97cf", "address": "172.17.17.1", ...},
    {"hwAddress": "90e2.ba5c.25fd", "address": "172.17.16.1", ...}
]
Why .items() Fails on a List
The .items() method belongs strictly to dictionary objects. It does not exist on lists.

If you tried to write:

Python
for x, y in arp_entries.items():  # CRASH!
Python would immediately halt and throw an AttributeError: 'list' object has no attribute 'items'.

'''

'''

There is no .append() here.

This difference highlights a fundamental rule of Python data structures: .append() only works on Lists, but here we are building a Dictionary.

Why the Syntax is Different
Lists use .append(): A list is just a flat sequence of individual items (like your ipv4_list = []). When you use .append(), you are just dropping a single piece of data onto the very end of the line.

Dictionaries use Assignment [key] = value: A dictionary cannot just accept a single flat item. It must have pairs—a Key and a Value. Because of this, Python requires you to use square brackets to explicitly declare the relationship:
    '''
