'''
1. Create a Python program that uses Jinja2 to generate the below BGP configuration. Your template should be directly embedded inside of your program as a string and should use for the following variables: local_as, peer1_ip, peer1_as, peer2_ip, peer2_as.
router bgp 10
  neighbor 10.1.20.2 remote-as 20
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor 10.1.30.2 remote-as 30
    address-family ipv4 unicast


'''



from jinja2 import Template

bgp_config = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
    address-family ipv4 unicast

"""

bgp_vars = {
        "local_as": 10,
        "peer1_ip": "10.1.20.2",
        "peer1_as": 20,
        "peer2_ip": "10.1.30.2",
        "peer2_as": 30,
        }

my_template = bgp_config
j2_template = Template(my_template)
output = j2_template.render(**bgp_vars)
print(output)

'''
1. j2_template = Template(my_template)
This line takes your raw multi-line string (my_template) and parses it into a Jinja2 Template object.

Jinja2 scans the text for its specific syntax markers, identifying the variables wrapped in double curly braces (like {{ local_as }} and {{ peer1_ip }}).

It compiles this into an internal format ready to accept data.

2. output = j2_template.render(bgp_vars)
This is where the configuration is actually built. The key mechanism here is the double asterisk (), known as dictionary unpacking.

Instead of passing variables one by one like this:
render(local_as=10, peer1_ip="10.1.20.2", ...)

The bgp_vars syntax automatically unpacks your dictionary keys and values, passing them into the function as individual keyword arguments.

Jinja2 matches the incoming keys (local_as, peer1_ip, etc.) with the {{ ... }} placeholders inside the template and swaps them out with their corresponding values.
'''
