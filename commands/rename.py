description = "This command renames a given file"
usage = ["Rename FILENAME NEW_FILENAME: Renames FILENAME to NEW_FILENAME"]

import os

# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    filename = ""
    newFilename = ""
    if len(cmd) <= 2:
        filename = input("Enter the file name: ")
        newFilename = input("Enter new file name: ")

    else:
        filename = cmd[1]
        newFilename = cmd[2]
    if not os.path.exists(filename):
        print(f"{filename}: no such file")
        return
        
    os.rename(filename, newFilename)

        
# must have
def constructor():
    return {"description": description, "usage":usage, "exec": run}
