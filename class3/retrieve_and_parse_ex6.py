'''

root@rocket> show configuration interfaces | display xml
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/21.4R0/junos">
    <configuration junos:commit-seconds="1782242259" junos:commit-localtime="2026-06-23 12:17:39 PDT" junos:commit-user="root">
            <interfaces>
                <interface>
                    <name>ge-0/0/18</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                            </inet>
                        </family>
                    </unit>
                </interface>
                <interface>
                    <name>xe-0/2/2</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                                <address>
                                    <name>10.64.51.68/28</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
                <interface>
                    <name>xe-0/2/3</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <ethernet-switching>
                                <interface-mode>access</interface-mode>
                                <vlan>
                                    <members>197</members>
                                </vlan>
                            </ethernet-switching>
                        </family>
                    </unit>
                </interface>
            </interfaces>
    </configuration>
    <cli>
        <banner>{master:0}</banner>
    </cli>
</rpc-reply>


In this labm we are going to use PyEZ library and extract interface names.
PyEZ usses NETCONF, port 830. This uses xml format RPC call. Hence it becomes easier to parse data. Thisis alt to cisco CONFPARSE

'''

import yaml

from jnpr.junos import Device #JNPR equivalent fo ConnectHandler
from jnpr.junos.exception import ConnectError #Exceptin handling

if __name__ == "__main__":
  filename = ".netmiko.yml"
  with open(filename) as f:
    yaml_out = yaml.safe_load(f)

  dut = yaml_out["ex_rocket"] #this is dict of dict. when we do ex_rocket here, we get the inner dict
  print("DUT type")
  print(type(dut))
  print("DUT content")
  print(dut)
  #dut is a dict, this is becasue yaml file itself has a dict. safe load method is a translator that keeps the data structure format as it is.If yam had a list, dut would also have been a list
  #
  #
  #This block is required because the Juniper PyEZ library (jnpr.junos.Device) doesn't automatically know how your YAML file is structured. It expects a specific set of parameters to establish a NETCONF session.This configuration block acts as a translator and translator-bridge between two different formats:1. Translating Your YAML Names to PyEZ NamesYour .netmiko.yml file uses standard Netmiko key names (like username), but Juniper PyEZ expects different key names (like user). This dictionary maps your YAML data to the exact keywords PyEZ requires:Your YAML has "username" $\rightarrow$ PyEZ requires "user"
  #
  #
  COMMON_SETTINGS = {
    "host": dut["host"],
    "user": dut["username"],
    "password": dut["password"],
    "port": 830,
  }
#
  try:
    with Device(**COMMON_SETTINGS) as dev:
      config_data = dev.rpc.get_config(filter_xml="<configuration><interfaces/></configuration>") # we are using xml calls in both directions
  except ConnectError as err:
    print(f"Connection failed {err}")
    exit(1)
  interfaces_container = config_data.find("interfaces") # we are INSIDE interfaces tag
  interface_list = interfaces_container.findall("interface") # we are inside interface tag
  #Because config_data is the <configuration> tag itself.

#he .find() method looks inside the current tag for its children. It does not look at itself.Hence w dont have find(config). thats how xml works. wihtr config_data, we are inside the <config> tab in XML

  print("Print Interfaces_Container")
  print(interfaces_container)
  print("Print its type")
  print(type(interfaces_container))
  # I have a separte note on find and findall in word doc

  for int in interface_list:
      print("\n\n\n")
      print(f" - Interface is: {int.findtext('name')}")

      #Now we need to search for units that may be more tha one. So we need findall inside the interface hierarchy.

      unit_list = int.findall("unit") #. this wil return pointers to all units inside that interface

      for unit in unit_list:
          unit_name = unit.findtext("name")#this wil return "zero 0" string. actually not required so commented it out
          #L3 address extraxction
          l3_address = unit.find("family/inet") #find wil return pointer
          if l3_address is not None:
              ip = l3_address.findtext("address/name") #find text will retunr actual text
              print(f" unit {unit_name} IP :{ip}")

          vlan_family = unit.find("family/ethernet-switching/vlan/members") #interface-mode is not specified as it shares same heirarchy as vlan
          if vlan_family is not None:

              vlan_id = vlan_family.text # here we are jsut doing 'text' as we are alredy in right hierarchy. so just converting pointer to text
              print(f"vlan id is {vlan_id}")

# two diff method of accessing text
          

'''

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^FINAL OUTPUT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
python3 retrieve_and_parse_ex6.py 
DUT type
<class 'dict'>
DUT content
{'device_type': 'juniper_junos', 'host': '10.85.173.165', 'username': 'python', 'password': 'Python'}
Print Interfaces_Container
<Element interfaces at 0x78e404f2a680>
Print its type
<class 'lxml.etree._Element'>




 - Interface is: ge-0/0/18
 unit 0 IP :None




 - Interface is: xe-0/2/2
 unit 0 IP :10.64.51.68/28




 - Interface is: xe-0/2/3
vlan id is 197

 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here is a line-by-line breakdown of your code, focusing heavily on how it traverses and extracts the specific XML structures returned by Junos.

Part 1: Connecting and Fetching Data
Python
  try:
    with Device(**COMMON_SETTINGS) as dev:
      config_data = dev.rpc.get_config(filter_xml="<configuration><interfaces/></configuration>")
Device(COMMON_SETTINGS): Unpacks your credentials dictionary to open a NETCONF session over TCP port 830.

dev.rpc.get_config(...): Sends an XML request asking the device to return only the [edit interfaces] hierarchy.

config_data: The device replies with a structured XML response. PyEZ drops the outer <rpc-reply> tags and hands you the <configuration> tag directly. config_data is an lxml.etree._Element object representing the <configuration> root box.

Part 2: Navigating the XML Tree
Python
  interfaces_container = config_data.find("interfaces")
config_data.find("interfaces"): The .find() method searches exactly one level down inside the <configuration> element for a tag named <interfaces>.

interfaces_container: It holds a memory pointer to that single <interfaces> block.

Python
  interface_list = interfaces_container.findall("interface")
interfaces_container.findall("interface"): Standing inside the <interfaces> element, .findall() scans for every child tag named <interface>.

interface_list: This becomes a standard Python list containing memory pointers to each individual interface block. Based on your target output, it tracks three pointers:

Pointer to the element for ge-0/0/18

Pointer to the element for xe-0/2/2

Pointer to the element for xe-0/2/3

Part 3: Printing Containers and Types
Python
  print("Print Interfaces_Container")
  print(interfaces_container)
  print("Print its type")
  print(type(interfaces_container))
print(interfaces_container): Printing an lxml element directly doesn't print raw text or JSON. It outputs its memory reference representation, looking something like <element interfaces at 0x... >.

type(interfaces_container): This will explicitly print <class 'lxml.etree._Element'>, proving that you are interacting with native XML objects and not a standard Python dictionary.

Part 4: The Loop and Data Extraction
Python
  for int in interface_list:
      print(f" - Interface is: {int.findtext('name')}")
for int in interface_list:: This loop steps through your list of pointers one by one. In each iteration, the variable int points directly to an isolated <interface> XML subsection.

int.findtext('name'): This is a powerful shortcut method. Instead of navigating manually using .find('name') and then extracting .text, .findtext('name') searches for the <name> tag inside that specific interface block and directly returns the string value stored within it.

Loop Execution Path (Using Your XML Output)
Iteration 1:
int points to the first block:

XML
<interface>
    <name>ge-0/0/18</name>
    ...
</interface>
int.findtext('name') evaluates to "ge-0/0/18".

Prints:  - Interface is: ge-0/0/18

Iteration 2:
int points to the second block:

XML
<interface>
    <name>xe-0/2/2</name>
    ...
</interface>
int.findtext('name') evaluates to "xe-0/2/2".

Prints:  - Interface is: xe-0/2/2

Iteration 3:
int points to the third block:

XML
<interface>
    <name>xe-0/2/3</name>
    ...
</interface>
int.findtext('name') evaluates to "xe-0/2/3".

Prints:  - Interface is: xe-0/2/3

⚠️ One Quick Python Warning
You used int as your loop variable name (for int in interface_list:). While this executes completely fine, int is a reserved built-in function in Python used for converting things to integers (e.g., int("10")). Overwriting it in a loop shadow-binds it, which can cause unexpected errors later in a larger script. It is always safer to use an alternative name like for intf in interface_list: or for interface in interface_list:.


@@@@@@@@@@@@@@@@@@@@@@@

why cant we use .find here instead of findtext


You actually can use .find() here! However, if you switch to .find(), you have to add an extra step to get the exact same output.

Here is the difference between why .findtext() is shorter and what happens if you use .find() instead.

.find() returns the whole XML Box
If you use .find("name"), Python returns the entire XML Element object (the tag container), not the text inside it.

If you write it like this:

Python
for intf in interface_list:
    print(f" - Interface is: {intf.find('name')}")
Your output will look like this broken mess:

Plaintext
 - Interface is: <element name at 0x7f981100>
To get the actual name string (like ge-0/0/18) using .find(), you have to explicitly ask for the .text attribute at the end of it:

Python
for intf in interface_list:
    # 🛑 Notice the .text at the end!
    print(f" - Interface is: {intf.find('name').text}")
.findtext() is a Built-in Shortcut
.findtext('name') is simply a convenient shortcut combination. It does two jobs in one single command:

It runs .find('name') to locate the tag box.

It automatically extracts the .text from inside it and hands you the string directly.

Summary
Both of these lines do the exact same thing under the hood:

The long way: intf.find('name').text

The short way: intf.findtext('name')

Engineers prefer .findtext() because it keeps the code cleaner, shorter, and avoids hitting an error if a tag happens to be completely missing.

'''
