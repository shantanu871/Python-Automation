from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

COMMON_SETTINGS = {
        'device_type': 'juniper_junos',
        'username': 'python',
        'password': 'Python',
        }

IP_LIST = ['10.85.173.215']

for IP in IP_LIST:
    print("\n================")
    print(f"processing switch: {IP}" )
    print("\n================")

    try:
        with ConnectHandler(**COMMON_SETTINGS, host = IP) as ssh_conn:
            print(f"Connection successful to : {IP}")

            cmd = 'show lldp neighbors'
            output = ssh_conn.send_command(cmd, strip_command=False, strip_prompt=False)
            print("*" *50)
            print(output)
    except NetmikoAuthenticationException:
            print(f"Error: Authentication for : {IP}")
    except NetmikoTimeoutException:
            print(f"Error: Timeout for :{IP}")
    except Exception as e:
            print(f"Unexpected error for {IP} : {e}")
       
