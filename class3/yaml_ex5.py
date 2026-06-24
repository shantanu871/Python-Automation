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

'''
safe load

When you deal with files in Python, you have to read them from disk into system memory. The line yaml.safe_load(f) is the exact mechanism that converts a raw text file into something Python can dynamically read.

Here is the breakdown of exactly what that function does line-by-line and why we choose it over the standard alternatives.

Mechanically: From Text to Object
When you run with open(".netmiko.yml") as f:, the variable f is not data yet. It is just an open stream or a "pointer" to a text file sitting on your hard drive. If you try to run loops or index lookups directly on f, Python will fail because it just sees a stream of characters.

yaml.safe_load(f) acts as the translator. It reads the string structure from the file stream f and deserializes it directly into a native Python data structure—in this case, a nested dictionary.

Plaintext
  [ Raw Text File: .netmiko.yml ]
        juniper1:
          host: 10.1.1.1
                 │
                 │  ( Passed through yaml.safe_load )
                 ▼
  [ Native Python Dictionary Object ]
        {"juniper1": {"host": "10.1.1.1"}}
Once parsed by safe_load(), you can instantly dive into your data using keys: yaml_out["juniper1"]["host"].

Why safe_load and not just load?
If you look at old Python examples online, you might see people using yaml.load(f). In modern automation, never use standard yaml.load().

The standard yaml.load() function is highly powerful—too powerful. It permits the YAML file to execute complex Python code or instantiate arbitrary objects directly inside your application when it parses.

The Security Trap: If a malicious user gets access to your inventory file and embeds a line of rogue code inside the text configuration, a standard yaml.load() function will run that code with whatever operating system privileges your script has. It could open an unauthorized reverse-shell straight out of your machine.

The safe_load Shield: yaml.safe_load() completely disables the execution engine. It strictly parses basic standard data types—like strings, numbers, lists, and standard key-value dictionaries. If someone attempts to inject hidden scripts or complex code execution into your YAML file, safe_load() throws a safe error and halts immediately.

It is a non-negotiable security habit for production automation pipelines. It ensures that your scripts handle configurations safely without introducing any execution vulnerabilities to the server running them.

'''

