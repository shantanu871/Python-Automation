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
