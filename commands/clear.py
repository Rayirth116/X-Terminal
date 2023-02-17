description = "This command clears the entire screen"
usage = ["clear: Clears the screen"]

# must have
import os
def run(args: str, ro_path:str):
   _ = os.system("clear")


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
