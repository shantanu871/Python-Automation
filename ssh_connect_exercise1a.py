from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# Define global credentials

COMMON_SETTINGS = {
        'device_type': 'juniper_junos',
        'username': 'python',
        'password': 'Python',
        'conn_timeout': 3,
}


# List of IPs

IP_LIST = ['10.85.173.215', '1.1.1.1']

#Loop through IPs for SSH

for ip in IP_LIST:
    print("\n=============================")
    print(f"Processing switch {ip}")
    print("===============================")
    
    try:
      with ConnectHandler(**COMMON_SETTINGS, host=ip) as ssh_conn:
        print(f"Connected to {ip}")
 
        command = "show version | match Junos:"
        print(f"Executing: {command}")
        output = ssh_conn.send_command(command)
        print(output)

    except NetmikoTimeoutException:
        print(f"Error: COnnection to {ip} timed out. Check routing or managememnt ip")

    except NetmikoAuthenticationException:
        print(f"Auth failed")
#Belwo is catch all
    except Exception as e:
       print(f"Unexpected error occured on {ip}: {e}")

####
#Exception is the Class
#Exception is the master blueprint for almost every error that can happen when a script runs. In Python, errors are structured in a family tree (a hierarchy), and Exception sits right near the top.

#Because it is the master class, catching Exception means you are catching a massive umbrella of errors, including:

#ZeroDivisionError (trying to divide by zero)

#IndexError (trying to pull an item from a list that doesn't exist)

#KeyError (looking for a dictionary key that isn't there)

#NetmikoTimeoutException (Netmiko's custom connection error)

print("\n All devices have been processed")
