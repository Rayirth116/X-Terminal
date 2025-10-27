# X-Terminal
A simple shell (command prompt) made in python featuring a command handler.

## Requirements
- Note: Python will be automatically downloaded by Rye
- [Rye](github.com/mitsuhiko/rye)

## Compatibility
Works and was tested on the following environments:
- Windows
- Linux

Note that it should work under MACOS too but wasn't tested

## Install
1) Clone using git (or download zip using the green button): `git clone https://github.com/Rayirth116/X-Terminal`
2) Change directory to X-Terminal: `cd X-Terminal`
3) Install the requirements using Rye: `rye sync`
4) Run shell.py `rye run python shell.py`

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

This project was founded by [Rayirth](https://github.com/Rayirth116) (Project Lead) and [Chaitanya](https://github.com/Chaitanya00Kumar), who contributed to the core and foundational structure of the code. Over time, the project has grown through the valuable efforts of multiple contributors, including [0x4c756e61](https://github.com/0x4c756e61), who provided major contributions, and Dart, who has supported the project through additional development work.

All ownership and rights to the repository and its code are retained by Rayirth as the project lead, regardless of contribution size.  
This project is open source and licensed under the **GNU General Public License v3.0 or later (GPLv3+)**.

