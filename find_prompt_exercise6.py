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
    print("Finding current prompt")
    print("#" *80)
    print(ssh_conn.find_prompt())

    print("#" *80)
    print("Entering into config mode")
    ssh_conn.config_mode()
    print(ssh_conn.find_prompt())
    print("#" *80)
    print(" exit config mode")
    ssh_conn.exit_config_mode()

    print(ssh_conn.find_prompt())
    print("#" *80)
