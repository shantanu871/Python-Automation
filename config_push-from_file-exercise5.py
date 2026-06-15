#Send confog from file

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

COMMON_SETTINGS = {
  'device_type': 'juniper_junos',
  'username': 'python',
  'password': 'Python',
}

IP_LIST = ['10.85.173.215']

for ip in IP_LIST:
    ssh_conn = ConnectHandler(**COMMON_SETTINGS, host = ip)
    output = ssh_conn.send_config_from_file("intf.txt")
    print(output)
