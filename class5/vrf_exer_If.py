from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise3/")

j2_vars = {"vrf_name": "blue", "rd_value": "100:1", "rt_value": "100:1", "ipv4_af": True, "ipv6_af": False}

print()
template_file = "ios_vrf.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars)
print(cfg)
print()

'''
when both true

(.venv) root@ubuntu:~/Python-Automation/class5# python3 vrf_exer_If.py

vrf def blue
!
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 exit-address-family
 !
 address-family ipv6
  route-target export 100:1
  route-target import 100:1
 exit-address-family
~

(.venv) root@ubuntu:~/Python-Automation/class5# vim vrf_exer_If.py
when one False

(.venv) root@ubuntu:~/Python-Automation/class5# python3 vrf_exer_If.py

vrf def blue
!
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 exit-address-family
 !
~

(.venv) root@ubuntu:~/Python-Automation/class5# ^C
(.venv) root@ubuntu:~/Python-Automation/class5#
'''
