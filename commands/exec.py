description = "Invoke system shell (CMD, POWERSHELL, SH etc..) to execute the provided command"
usage = [
        "exec COMMAND: Executes COMMAND using the system shell",
        "exec firefox: Runs firefox using the system shell"
        ]

import os
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    if len(cmd) < 2:
        print("Missing argument SYSTEM_COMMAND")
        return

    _ = os.system(" ".join(cmd[1:]))


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}