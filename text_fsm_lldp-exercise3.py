
"""
Technical Problem Summary: TextFSM State Mismatch
The Problem:
The script execution failed with a textfsm.parser.TextFSMError: State Error raised. This occurred because the ntc-templates library (used by Netmiko's use_textfsm=True) employs a strict Regular Expression (Regex) state machine to parse CLI output.

When executing show version on the target Junos device, the output began with two lines that were not defined in the corresponding TextFSM template's logic:

localre:

--------------------------------------------------------------------------

Because the TextFSM parser encountered this unexpected header, it failed to transition to the expected state (mapping Hostname, Model, etc.), resulting in a hard crash of the automation script.

Solution 1: Graceful Fallback (Error Handling)
Wrap structured parsing calls in a try-except block. This allows the script to catch TextFSMError exceptions and immediately re-execute the command using raw text capture, ensuring the automation suite remains operational even when a template is missing or incompatible.


   # Before sending to Netmiko, or by modifying the raw output:
    raw_output = ssh_conn.send_command("show version")
    # Remove the first two lines (localre: and the dash line)
    clean_output = "\n".join(raw_output.splitlines()[2:]) 

    # Now pass the clean_output to your parser logic, or 
    # if you really want TextFSM, you'd need to write a custom rule

Solution 2: Model-Driven Output (JSON/XML)
Bypass TextFSM parsing entirely for commands that support it. Use the Junos CLI pipe operator: show version | display json. This forces the device to return data in a standard, schema-compliant JSON format, which eliminates reliance on volatile Regex templates and provides a robust, future-proof data structure.

"""



from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

COMMON_SETTINGS = {
        "device_type": "juniper_junos",
        "username": "python",
        "password": "Python",
}

IP_LIST = ["10.85.173.215"]

for IP in IP_LIST:
    try:
        with ConnectHandler(**COMMON_SETTINGS, host = IP) as ssh_conn:
            print("+" *50)
            print(f" Connection succesful to : {IP}")
            print("+" *50)

            cmd_list = ["show lldp neighbors","show arp no-resolve"]

            for cmd in cmd_list:
                output = ssh_conn.send_command(cmd, use_textfsm=True, )
                print("="*80)
                #When you use use_textfsm=True, the output variable will no longer be a string; it will be a list of dictionaries.
                print(f"PRINT RAW TEXT FSM OUTPUT for {cmd}") 
                print(output)
                print("="*80)

                if cmd == "show lldp neighbors":
                    print("*" *50)
                    print("LLDP Data structure type is {}:".format(type(output)))
                    print("*" *50)
                    print("Spine01 interface is {}:".format(output[6]["neighbor_interface"]))
                    #NOtice, above we used neighbor_interface althigyu this doenst exost in CLI command. We need to go per NTC template
                    print("*" *50)

    except NetmikoAuthenticationException:
        print(f"Auth error for {IP}")

    except NetmikoTimeoutException:
        print(f"Timeout for :{IP}")



