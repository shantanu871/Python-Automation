import json

with open("nxos_interfaces.json") as f:
    nxos_data = json.load(f)

ipv4_list =[]
ipv6_list = []

for intf, ipaddr_dict in nxos_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
             ipv4_list.append(f"{ip_addr}/{prefix_length}")
            elif ipv4_or_ipv6 == "ipv6":
             ipv6_list.append(f"{ip_addr}/{prefix_length}")

print("\n IPv4 ADDR is :{}\n".format(ipv4_list))
print(f"\n IPv6 ADDR is : {ipv6_list}")


'''
Here is a clear summary of how the .items() method works based on our breakthrough during this exercise.

The absolute golden rule to remember for Python dictionaries is Dictionary Unpacking. When you combine a for loop with .items(), Python mechanically splits that layer of the dictionary down the middle at the very first colon (:) of that level.

The Left vs. Right Rule
for x, y in dictionary.items():
    x (The Left Side): Always receives the Key (usually a plain text string label).

y (The Right Side): Always receives the Value (which can be a string, an integer, a list, or an entire nested dictionary).

How it Applied to Your Triple-Nested Loop
Kirk’s script used this exact left/right slicing mechanic three times in a row, tunneling deeper into the JSON structure with each step:

    Layer 1: The Interface Level
    for intf, ipaddr_dict in nxos_data.items():

    Left (intf): "Ethernet2/3"

Right (ipaddr_dict): The entire internal dictionary block containing both protocol families.

Layer 2: The Protocol Level
Python
for ipv4_or_ipv6, addr_info in ipaddr_dict.items():

    eft (ipv4_or_ipv6): "ipv4" or "ipv6"

Right (addr_info): The dictionary of IP addresses belonging only to that address family.

Layer 3: The IP Address Level
Python
for ip_addr, prefix_dict in addr_info.items():
Left (ip_addr): The raw IP string (e.g., "4.4.4.4" or "2001:db8::1").

Right (prefix_dict): The final innermost dictionary holding the attributes: {"prefix_length": 16}.

The Massive Benefit of .items()
By letting .items() dynamically discover what keys exist on the left side of the colon at every layer, the code never explicitly requests a key by name (like trying to force data["ipv4"]).

This is why the code seamlessly bypasses interfaces like Ethernet2/4 that lack IPv4 entirely. Python simply loops through whatever keys .items() uncovers, completely eliminating the risk of a KeyError crash!
'''

