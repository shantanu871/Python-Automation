'''

we are going to call bgp.j2 and vlans.j2 template from parant.j2 template
'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise5/")

j2_vars = {"ip_address": "192.168.1.1", "vlan_id":"22", "bgp_type":"external"}

template_file = "parent.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars)
print(cfg)
