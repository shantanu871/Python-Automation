from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise4")

my_vrfs = [
          {"vrf_name": "blue1", "rd_number": "100:1", "ipv4_af": True, "ipv6_af": True},
          {"vrf_name": "blue2", "rd_number": "100:2", "ipv4_af": True, "ipv6_af": True},
          {"vrf_name": "blue3", "rd_number": "100:3", "ipv4_af": True, "ipv6_af": True},
          {"vrf_name": "blue4", "rd_number": "100:4", "ipv4_af": True, "ipv6_af": True},
          {"vrf_name": "blue5", "rd_number": "100:5", "ipv4_af": True, "ipv6_af": True},
]

j2_vars = { "my_vrfs": my_vrfs }
#we cant pass only Dict in templ;ate rendering . my_vars was a lsit of dict, now we created dict of a list of dict.

template_file = "multi_vrf.j2"
template = env.get_template(template_file)
cfg = template.render(**j2_vars) #The double asterisk () in Python is called the dictionary unpacking operator (or "double splat").
print(cfg)
'''
root@ubuntu:~/Python-Automation/class5# python3 multivrf.py

vrf def blue1
 !
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 !
  address-family ipv6
   route-target export 100:1
   route-target import 100:1
  exit-address-family
vrf def blue2
 !
 address-family ipv4
  route-target export 100:2
  route-target import 100:2
 !
  address-family ipv6
   route-target export 100:2
   route-target import 100:2
  exit-address-family
vrf def blue3
 !
 address-family ipv4
  route-target export 100:3
  route-target import 100:3
 !
  address-family ipv6
   route-target export 100:3
   route-target import 100:3
  exit-address-family
vrf def blue4
 !
 address-family ipv4
  route-target export 100:4
  route-target import 100:4
 !
  address-family ipv6
   route-target export 100:4
   route-target import 100:4
  exit-address-family
vrf def blue5
 !
 address-family ipv4
  route-target export 100:5
  route-target import 100:5
 !
  address-family ipv6
   route-target export 100:5
   route-target import 100:5
  exit-address-family

root@ubuntu:~/Python-Automation/class5#

'''
