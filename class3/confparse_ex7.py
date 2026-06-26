from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""
# When feeding config directly - CiscoConfParse requires a list
# ignore_blank_lines=False so that ciscoconfparse does not emit logging message to stderr

conf_list = bgp_config.splitlines()
bgp_parse = CiscoConfParse(conf_list, ignore_blank_lines = False)

# create an empty list

bgp_peers = []
neighbors = bgp_parse.find_objects_w_parents(
        parentspec = r"router bgp", childspec = r"neighbor"
        )

print("NEIGHBORS_PARSED LIST_CONFPARSE")
print(neighbors)
print("\n\n")

#Find me lines that match the word neighbor (childspec), but only if they live inside a configuration block that starts with router bgp (parentspec)." This returns a list of matching configuration line objects.

for neighbor in neighbors:
    _, neighbor_ip = neighbor.text.split()
    print(f"neighbor IP is: {neighbor_ip}")
    print("\n\n")
    for child in neighbor.children:
        if "remote-as" in child.text:

          _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))#this wil guive tuple. for list we can use []
print("\n\n")
print("BGP Peers:")
print(bgp_peers)
print("\n\n")
    

'''
# ===============================================================================
# HOW THIS NESTED LOOP EXTRACTS THE CHILD DATA:
#
# 1. 'neighbors' is a list of smart objects returned by ciscoconfparse.
# 2. Each object has a '.text' attribute (the parent line string).
# 3. Each object has a '.children' attribute (a list of its indented sub-lines).
#
    # Extracts parent line (e.g., " neighbor 10.220.88.20") and splits out the IP
    _, neighbor_ip = neighbor.text.


# ===============================================================================

for neighbor in neighbors:
    # Extracts parent line (e.g., " neighbor 10.220.88.20") and splits out the IP
    _, neighbor_ip = neighbor.text.split()
    print(f"neighbor IP is: {neighbor_ip}")
    print("\n\n")

    # GUARDRAIL: Reset variable so data from neighbor #1 doesn't bleed into neighbor #2
    remote_as = None

    # INNER LOOP: Steps inside the parent object to look at its indented child lines
    # (e.g., [ '  remote-as 42', '  description pynet-rtr1', '  address-family...' ])
    for child in neighbor.children:

        # Checks if the string "remote-as" exists anywhere on this specific child line
        if "remote-as" in child.text:

            # Splits "  remote-as 42" into ['remote-as', '42'] and captures the AS number
            _, remote_as = child.text.split()

            # OPTIMIZATION: We found our target line, stop looping through remaining children
            break

    # Append the combined pair as a tuple inside your master tracking list
    bgp_peers.append((neighbor_ip, remote_as))
    '''

