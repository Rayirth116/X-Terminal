description = "This command is used to probe an IP address"
usage = [
        "ping IPV4: Probes the provided IPV4 address",
        "ping google.com: Check if you can reach google"
        ]

# must have
import os
from colorama import Fore
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    hostname = ""
    if len(cmd) == 2:
        hostname = cmd[1]
    else:
        hostname = input("address: ")

    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        print(" ")
        print(Fore.LIGHTGREEN_EX + hostname, 'is up!')
    else:
        print(" ")
        print(Fore.LIGHTRED_EX + hostname, 'is down!')


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
