# Py-Shell
A simple shell (command prompt) made in python featuring a command handler.

## Requirements
- Python3

## Compatibility
Works and was tested on the following environments:
- Windows
- Linux

Not that it should work under MACOS too but wasn't tested

## Install
1) Clone using git (or download zip using the green button): `git clone https://github.com/0x454d505459/Py-Shell`
2) Change directory to Py-Shell: `cd Py-Shell`
3) Run shell.py `python3 shell.py`

## Adding commands
### Adding external commands

- Change into the `commands` directory
- Copy the `template.txt` as `<command_name>.py` (make sure you replace `<command_name>` with the command's name, this will be used by the command handler to invoke it)
- Fillin the required variables located at the top (`description` and `usage`, if command doesn't have any usage examples, leave usage empty)
- Start coding

#### Notes
- the `run` function will be executed every time the command is entered in the shell, put any code needing to be ran multiple times here
- `ro_path` argument is read_only, changing it won't affect the path
- `constructor` is a MUST HAVE function, it will be called by the command handler to get the necessary informations to run the command, it will be called only at startup
- `run` also is a MUST HAVE, you can rename it if you want but make sure changes are reflected in the `constructor` function
- All imports should be outside of the run function

## Licensing
All commits made by Me ([0x454d505459](https://github.com/0x454d505459)) fall under GPLv3 and Later licenses. For other commits please contact their commiters.