
'''

2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices. 
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?

'''

import yaml
from pprint import pprint

leaf1 = {"device_name": "leaf1", "host" : "10.83.173.215"}
leaf2 = {"device_name": "leaf2", "host" : "10.83.173.217"}

device_list = [leaf1, leaf2]

for device in device_list:
    device["username"] = "python"
    device["password"] = "Python"
pprint(device_list)

'''
.Python does not make copies of your dictionaries. Instead, device_list is a list of pointers (references) pointing directly to the original leaf1, leaf2, etc., objects sitting in your RAM.

When your loop executes:
device becomes a temporary pointer to the active dictionary
 (e.g., leaf1).

device["username"] = "admin" modifies that dictionary 
directly in your system's memory.

Because it modifies the data in-place,
 those  new credentials are permanently added to your data.
 '''
with open("my_devices.yml", "w") as f:
    yaml.dump(device_list, f, default_flow_style= False)


'''

The Context Manager (with open(...) as f:)
Using with open() is the best-practice method for file handling in Python.

"my_devices.yml": This is the filename you are targeting. If the file doesn't exist, Python will automatically create it in your current directory (~/Python-Automation/). If it does exist, Python will completely overwrite it.

"w": This stands for Write Mode. It opens the file stream strictly for writing text data.

as f: This creates a temporary file object variable named f that points to that active file stream.

The Magic: The moment the indented block underneath finishes executing, the context manager automatically closes the file stream behind the scenes. This prevents memory leaks and file corruption, even if your script crashes.

2. Slicing the YAML Method (yaml.dump(...))
The yaml.dump() function translates Python native objects (like lists and dictionaries) into a standard text stream format that human network operators can read.

my_devices: This is your source data payload (the list containing your 4 updated device dictionaries).

f: This is the destination file object you opened in write mode. You are telling Python: "Dump the translated data right into this file stream."

3. Controlling the Layout (default_flow_style=False)
This is a critical parameter when dealing with network engineering configuration structures:

If default_flow_style=True (or omitted in older versions): YAML will use its "inline" format, which uses brackets and looks a lot like Python JSON output:


[{device_name: leaf1, host: 10.83.173.215, {device_name: leaf2, host: 10.83.173.217}]
'''


