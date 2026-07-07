from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise2")

interface = "ge-0/0/26"

jnpr1 = {"device_name": "Rocket", "local_as": "22", "interface": interface, "ipv4_address": "10.1.100.1", "ipv4_netmask": "24"}
jnpr2 = {"device_name": "Simba", "local_as": "22", "interface": interface, "ipv4_address": "10.1.100.2", "ipv4_netmask": "24"}

jnpr1["peer_ip"] = jnpr2["ipv4_address"]
jnpr2["peer_ip"] = jnpr1["ipv4_address"]

for J2_vars in (jnpr1, jnpr2):
    print(f"{J2_vars['device_name']}".center(80, "#"))
    template_file = "junos_bgp.j2"
    temp_env = env.get_template(template_file)
    temp_render = temp_env.render(**J2_vars)
    print(temp_render)
'''
(.venv) root@ubuntu:~/Python-Automation/class5# python3 ex2b_junos.py
#####################################Rocket#####################################
set interfaces ge-0/0/26 family inet address 10.1.100.1/24
set protocols bgp group INTERNAL-PEERS type internal
set protocols bgp group INTERNAL-PEERS local-as 22
set protocols bgp group INTERNAL-PEERS neighbor 10.1.100.2
#####################################Simba######################################
set interfaces ge-0/0/26 family inet address 10.1.100.2/24
set protocols bgp group INTERNAL-PEERS type internal
set protocols bgp group INTERNAL-PEERS local-as 22
set protocols bgp group INTERNAL-PEERS neighbor 10.1.100.1
'''
