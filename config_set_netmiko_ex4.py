"""
We wil use config_set to push multiple config lines so for loop is not required.
Also, we wil experiment wit fast cli
"""

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from datetime import datetime

start_time = datetime.now()
COMMON_SETTINGS = {
        "device_type": "juniper_junos",
        "username": "python",
        "password": "Python",
        "fast_cli": False,
}

IP_LIST = "10.85.173.215"

net_connect = ConnectHandler(**COMMON_SETTINGS, host = IP_LIST)
cmd = ["set interfaces xe-0/0/38 description TEST", "set interfaces xe-0/0/38 unit 0 family inet address 192.168.250.255/32"]
output = net_connect.send_config_set(cmd)
print("#" *80)
print(output)
print("#" *80)

end_time = datetime.now()
print(f"start time is {start_time}")
print(f"End time is : {end_time}")

print("Time taken to execution is :{}".format(end_time - start_time))

"""
we can see fat clie does help
(.venv) root@ubuntu:~/Python-Automation# python3 config_set_netmiko_ex4.py 
################################################################################
configure 
Entering configuration mode
Users currently editing the configuration:
  labroot terminal pts/0 (pid 11935) on since 2026-06-15 14:01:04 UTC, idle 00:21:07
      {master:0}[edit]
The configuration has been changed but not committed

{master:0}[edit]
python@ddtcdodcl01_a2_12789#set interfaces xe-0/0/38 description TEST 

{master:0}[edit]
python@ddtcdodcl01_a2_12789# set interfaces xe-0/0/38 unit 0 family inet address 192.168.250.255/32 

{master:0}[edit]
python@ddtcdodcl01_a2_12789# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
python@ddtcdodcl01_a2_12789> 
################################################################################
start time is 2026-06-15 07:05:36.084368
End time is : 2026-06-15 07:05:36.638814
Time taken to execution is :0:00:00.554446
(.venv) root@ubuntu:~/Python-Automation# vim config_set_netmiko_ex4.py
(.venv) root@ubuntu:~/Python-Automation# python3 config_set_netmiko_ex4.py 
################################################################################
configure 
Entering configuration mode
Users currently editing the configuration:
  labroot terminal pts/0 (pid 11935) on since 2026-06-15 14:01:04 UTC, idle 00:21:49
      {master:0}[edit]
The configuration has been changed but not committed

{master:0}[edit]
python@ddtcdodcl01_a2_12789#set interfaces xe-0/0/38 description TEST 

{master:0}[edit]
python@ddtcdodcl01_a2_12789# set interfaces xe-0/0/38 unit 0 family inet address 192.168.250.255/32 

{master:0}[edit]
python@ddtcdodcl01_a2_12789# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
python@ddtcdodcl01_a2_12789> 
################################################################################
start time is 2026-06-15 07:06:17.506009
End time is : 2026-06-15 07:06:18.598388
Time taken to execution is :0:00:01.092379


"""
ping_output = net_connect.send_command("ping 8.8.8.4 count 3", read_timeout = 20)
print(ping_output)

if "3 packets received" in ping_output:
    print("Ping succesful")
else:
    raise ValueError("Ping failed: {}".format(ping_output))


""""
Because you used raise ValueError("Ping failed: {}".format(ping_output)), Python wraps your custom message along with the entire console output of the ping into a single error payload.

When a script hits a raise statement, Python immediately interrupts the normal stdout stream (which prints clean text) and redirects everything to the stderr stream (which prints the red/white traceback log).



**************************************************************

End time is : 2026-06-15 07:32:58.601322
Time taken to execution is :0:00:01.105591
PING 8.8.8.4 (8.8.8.4): 56 data bytes

--- 8.8.8.4 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss

Traceback (most recent call last):
  File "/root/Python-Automation/config_set_netmiko_ex4.py", line 97, in <module>
    raise ValueError("Ping failed: {}".format(ping_output))
ValueError: Ping failed: PING 8.8.8.4 (8.8.8.4): 56 data bytes

--- 8.8.8.4 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss

**************************************************************
"""
