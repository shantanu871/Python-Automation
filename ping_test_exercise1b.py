from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

COMMON_SETTINGS = {
  'device_type': 'juniper_junos',
  'username': 'python',
  'password': 'Python',
}

IP_LIST = ['10.85.173.215']

for IP in IP_LIST:
    print("\n=================")
    print(f"processing switch: {IP}")
    print("\n=================")

    try:
       with ConnectHandler(**COMMON_SETTINGS, host = IP) as ssh_conn:
         print (f"connected to {IP}")
    
        # Code for PING
         output = ssh_conn.send_command_timing("ping 100.120.236.251 count 3", strip_prompt=True, strip_command=True)

        # ssh_conn.disconnect()<<<<<Not required.
         print(output)

    except NetmikoTimeoutException:
      print(f"Error: Connection to {IP} timedout")
    except NetmikoAuthenticationException:
      print(f"Auth error- {IP}")
    except Exception as e:
      print(f"Unexpected Error on {IP} : {e}")


