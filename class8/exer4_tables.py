"""
4. PYeZ configuration operations (Part 2):

4a. Using the previously created jnpr_devices.py file, open a connection to srx2 and gather the current routing table information.

4b. Using PyEZ stage a configuration from a file. The file should be "conf" notation. This configuration should add two static host routes (routed to discard). These routes should be from the RFC documentation range of 203.0.113.0/24 (picking any /32 in that range should be fine). Use "merge=True" for this configuration. For example:
routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}

4c. Reusing your gather_routes() function from exercise2, retrieve the routing table before and after you configuration change. Print out the differences in the routing table (before and after the change). To simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added. You can use either load() and set operations or load() plus a configuration file to accomplish this.
"""
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from exer2a_jnpr_devices import EX2
from exer2b_jnpr_tables import check_connected, gather_routes

#var that points to static route config

CONFIG_FILE = "static_routes.conf"

#Func to load merge routes from config file and commit
def route_config(path, dev, merge=True):
    #creat config object
    cfg = Config(dev)
    cfg.lock()
    cfg.load(path=path, format="text", merge=merge)
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()


def compare_routes(original_routes, added_routes):
    """Func to compare routes """
    print()
    print("Check for newly added routes")
    new_routes =[]
    for x in added_routes.keys():
        if x not in original_routes.keys():
            new_routes.append(x)
    return new_routes
"""
In Python and PyEZ, .keys() is a built-in method used on dictionaries (or dictionary-like table objects) to extract all the keys while ignoring the values.

In this specific function, .keys() plays a very important role:

What are the "Keys" in a PyEZ Route Table?
When gather_routes(device) pulls the routing table from the device, it returns a table view object. When treated like a dictionary:

The Keys are the IP route prefixes (e.g., 203.0.113.5/32, 10.0.0.0/24).

The Values are the route attributes (next-hop, protocol, metric, age, etc.).

Below is breakdown

for route in updated_routes.keys():
    if route not in initial_routes.keys():
        new_routes.append(route)

updated_routes.keys(): This grabs a list of every single IP prefix currently present in the routing table after you loaded your configuration file.

for route in ...: The loop iterates through each of those IP prefixes one by one.

if route not in initial_routes.keys(): It checks if that specific IP prefix existed in your original baseline route dictionary (initial_routes).

new_routes.append(route): If the prefix is present now, but was not present in the initial baseline, it gets added to your new_routes list as a newly introduced route.

Using .keys() allows the script to quickly compare just the IP addresses/prefixes without having to compare complex nested routing attributes or metadata.
"""

def rollback_routes(my_dev):
    cfg = Config(my_dev)
    cfg.lock()
    cfg.load("delete routing-options static route 203.0.113.5/32", format="set", merge=True)
    cfg.load("delete routing-options static route 203.0.113.200/32", format="set", merge=True)

    print("Deleting added static route")
    print("\n\n")
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()



if __name__ == "__main__":
    
#Belwo are function calls

    #open dev connection - 4a

    my_dev = Device(**EX2)
    my_dev.open()
    check_connected(my_dev)

    #Gather existing routes per 4a
    routes = gather_routes(my_dev)

    #Conf static routes
    route_config(CONFIG_FILE, my_dev)

    #Gather new routes for comparison

    updated_routes = gather_routes(my_dev)
    #Delta of routes
    new_routes = compare_routes(routes, updated_routes)

    print(f"{my_dev.hostname} has following newly added routes - {new_routes}")

    rollback_routes(my_dev)

"""
(.venv) root@ubuntu:~/Python-Automation/class8# python exer4_tables.py 
Password: 



Device 10.85.173.163 is connected

Check for newly added routes
10.85.173.163 has following newly added routes - ['203.0.113.5/32', '203.0.113.200/32']
Deleting added static route

"""
