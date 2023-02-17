description = "This command creates a new directory (folder)."

usage = [
        "mkdir NAME: Creates the directory NAME",
        "mkdir: Asks for the name of the directory to create"
        ]

import os
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    newdir = ""
    if len(cmd) == 2:
        newdir = cmd[1]
    else:
        newdir = input("directory name: ")

    newdir_path = os.path.join(ro_path, newdir)

    if os.path.exists(newdir_path):
        print(f"mkdir: {newdir} already exists")
        return

    os.mkdir(newdir_path)
    print("Directory '% s' created" % newdir)



# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
