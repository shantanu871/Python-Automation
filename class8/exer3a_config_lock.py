"""
WE USE ex2 INSTEAD OF srx FOR ALL LABS

3. PyEZ configuration operations (Part 1):

3a. Open a connection to the srx2 device and acquire a configuration lock. Validate that the configuration session is indeed locked by SSH'ing
 into the device and attempting to enter configuration mode ("configure"). Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following:
pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive
3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name python4life".

3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following:
[edit system]
-  host-name srx2;
+  host-name python4life;

3d. Rollback the staged configuration. Once again, print out the diff of the staged and the current configuration (which at this point should be None).
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from exer2a_jnpr_devices import EX2

"""
from jnpr.junos import Device: Imports the primary PyEZ class responsible for establishing and managing the NETCONF-over-SSH connection to a Junos device.

from jnpr.junos.exception import LockError: Imports PyEZ's custom exception class. This allows your script to catch specific errors raised when a configuration lock request is rejected because another session holds the lock.

from jnpr.junos.utils.config import Config: Imports the PyEZ utility class designed specifically for managing configuration tasks (locking, loading changes, diffing, committing, and rolling back).

from jnpr_devices import srx2: Imports your dictionary containing the connection parameters (IP address, username, password, etc.) for the target device.
"""

my_dev = Device(**EX2)
my_dev.open()

#create config object for device
cfg_dev = Config(my_dev)

cfg_dev.lock() #lock the dev config

print()
try:
    cfg_dev.lock()
    print("Lock acquired")
except LockError:
    print("Device is already locked")

print("-" *20)
#Stage config to set hostname

cfg_dev.load("set system host-name TEST", format = "set", merge = "True")

#check the diff- show compare
print("check the diff in config")
print("-" *20)

diff = cfg_dev.diff()
print(diff)

#rollback without commit

cfg_dev.rollback(0)

#check diff again, there should be none

print("-" *20)
print(" the diff is ...")
print(cfg_dev.diff())
print("-" *20)


"""
(.venv) root@ubuntu:~/Python-Automation/class8# python3 exer3a_config_lock.py
Password:

Device is already locked
--------------------
check the diff in config
--------------------

[edit system]
-  host-name simba;
+  host-name TEST;

--------------------
 the diff is ...
None
--------------------
(.venv) root@ubuntu:~/Python-Automation/class8# vim exer3a_config_lock.py
(.venv) root@ubuntu:~/Python-Automation/class8#

"""
