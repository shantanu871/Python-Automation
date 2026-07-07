from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise2")

interface = "Ethernet1/1"

nxos1 = {"device_name": "nxos1", "local_as": "22", "interface": interface, "ipv4_address": "10.1.100.1", "ipv4_netmask": "24"}
nxos2 = {"device_name": "nxos2", "local_as": "22", "interface": interface, "ipv4_address": "10.1.100.2", "ipv4_netmask": "24"}

nxos1["peer_ip"] = nxos2["ipv4_address"]
nxos2["peer_ip"] = nxos1["ipv4_address"]

for J2_vars in (nxos1, nxos2):
    print(f"{J2_vars['device_name']}".center(80, "#"))
    template_file = "nxos_bgp.j2"
    temp_env = env.get_template(template_file)
    temp_render = temp_env.render(**J2_vars)
    print(temp_render)

'''
#####################################nxos1######################################
interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
  address-family ipv4 unicast
#####################################nxos2######################################
interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
  address-family ipv4 unicast
(.venv) root@ubuntu:~/Python-Automation/class5#
'''
