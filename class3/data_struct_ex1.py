'''
1. Using the below ARP data, create a five element list.
 Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface".
 At the end of this process, you should have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

import re
from pprint import pprint

arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""

arp_data = arp_data.strip() #strip heading and trailing whitespaces
arp_data = arp_data.splitlines() #make ONE List of 6 items, separated by newline

print("*" *80)
print("ARP_DATA IN LIST FORMAT")
print(arp_data)

processed_list = [] # create empty list

for arp_entry in arp_data: #loop thruhg each item in the list ie, each line(saved as arp_entry)
 if re.search(r"^Protocol.*Interface", arp_entry): #we dont need first line (protocol, address etc), so once we hit it, move to next
     continue
 _, ip_addr, _, mac_addr, _, intf = arp_entry.split() 
 #split arp_entry by whitespaces and map it to variables defined on 1-1 basis. Indexation is preserved. THIS WILL NOT CREAT A LIST. THISIS CALL ITERABLE UNPACKING
 arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}
 processed_list.append(arp_dict)
 print("#" *80)
 pprint(processed_list)
 
 print("NOT PRETTY PRINT")
 print(processed_list)
 print()
print("!" *100)
pprint("Final list")
pprint(processed_list)
'''
Line 36 explnation
Python evaluates the assignment operator (=). It maps each item from that 6-element list directly to the 6 variables you provided on the left side, based on their index positions:

List Index    String Value        Assigned Variable
───────────────────────────────────────────────────────
    [0]       'Internet'       ──►  _         (Dummy variable, thrown away)
    [1]       '10.220.88.1'    ──►  ip_addr   (Saved!)
    [2]       '67'             ──►  _         (Dummy variable, overwritten)
    [3]       '0062.ec29.70fe' ──►  mac_addr  (Saved!)
    [4]       'ARPA'           ──►  _         (Dummy variable, overwritten)
    [5]       'GigabitEthernet0/0/0' ► intf     (Saved!)

'''

