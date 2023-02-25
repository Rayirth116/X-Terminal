description = "This commands lists all files and directories in the selected directory (default is current working one)"
usage = ["ls ..: Lists all files in the parrent directory"]

from colorama import Fore
import os
# must have
def run(args: str, ro_path):
    path = ro_path
    if len(args.split(" ")) > 1:
        path = " ".join(args.split(" ")[1:])
    try:
        for files in os.listdir(path):
            print(Fore.CYAN + '-' + files)
    except:
        print("Can't list directory: "+path)

# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
