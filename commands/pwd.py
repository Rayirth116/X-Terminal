description = "This command prints the current working directory"
usage = ["'pwd': The shell prints the directory you are working in."]

# must have
def run(args: str, ro_path:str):
    print(ro_path)

# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
