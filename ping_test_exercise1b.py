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
         output = ssh_conn.send_command_timing("ping 100.120.236.251 count 3", strip_prompt=False, strip_command=False)

        # ssh_conn.disconnect()<<<<<Not required.
         print(output)

    except NetmikoTimeoutException:
      print(f"Error: Connection to {IP} timedout")
    except NetmikoAuthenticationException:
      print(f"Auth error- {IP}")
    except Exception as e:
      print(f"Unexpected Error on {IP} : {e}")

"""Belwo is output

(.venv) root@ubuntu:~/Python-Automation# python3 ping_test_exercise1b.py 

=================
processing switch: 10.85.173.215

=================
connected to 10.85.173.215
PING 100.120.236.251 (100.120.236.251): 56 data bytes
64 bytes from 100.120.236.251: icmp_seq=0 ttl=64 time=4.088 ms
64 bytes from 100.120.236.251: icmp_seq=1 ttl=64 time=10.970 ms
64 bytes from 100.120.236.251: icmp_seq=2 ttl=64 time=6.183 ms

--- 100.120.236.251 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max/stddev = 4.088/7.080/10.970/2.880 ms

(.venv) root@ubuntu:~/Python-Automation# vim ping_test_exercise1b.py 
(.venv) root@ubuntu:~/Python-Automation# python3 ping_test_exercise1b.py 

=================
processing switch: 10.85.173.215

=================
connected to 10.85.173.215
ping 100.120.236.251 count 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<strip cmd = false
PING 100.120.236.251 (100.120.236.251): 56 data bytes
64 bytes from 100.120.236.251: icmp_seq=0 ttl=64 time=13.782 ms
64 bytes from 100.120.236.251: icmp_seq=1 ttl=64 time=11.782 ms
64 bytes from 100.120.236.251: icmp_seq=2 ttl=64 time=7.241 ms

--- 100.120.236.251 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max/stddev = 7.241/10.935/13.782/2.737 ms

{master:0}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<strip prompt = false
python@ddtcdodcl01_a2_12789> 
(.venv) root@ubuntu:~/Python-Automation# 
"""
