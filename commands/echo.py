description = "Prints the given text to the terminal"
usage = [
        "echo MESSAGE: Outputs MESSAGE to the screen",
        "echo Hello: Prints Hello"
        ]
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    toEcho = ""
    if len(cmd) > 1:
        toEcho = " ".join(cmd[1:])
    else:
        toEcho = input("What do you want to echo?: ")

    print(toEcho)


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
