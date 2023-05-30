# pvulnz

Public version of custom PHP static analysis helper tool.

It will print out 'dangerous' lines with functions defined inside 'functions.txt'.

## Install For Bash
`git clone https://github.com/hansmach1ne/pvulnz`  
`cd pvulnz/`  
`pDir=$(pwd)`  
`echo -e -n "\nalias pvulnz=\"python3 $pDir/pvulnz.py\"" >> ~/.bashrc`  
`source ~/.bashrc`  
`pip3 install -r requirements.txt`  
`pvulnz -h`  

## -h, --help
```
usage: pvulnz.py [-a <function>] [-d <function>] [-m] [-ms <string>] [-mr <regex>] [-r] [-h] [files ...]

pvulnz, PHP static analysis helper tool

positional arguments:
  file(s)          Specify php file(s) to look at, '*' for all.

optional arguments:
  -a <function>    Specify function name to add to the functions file
  -d <function>    Specify function name to delete from the functions file
  -m               Turn on match mode, while in this mode, 'functions.txt' is ignored
  -ms <string>     Specify string to match from parsed files.
  -mr <regex>      Specify regex string to match from parsed files.
  -r, --recursive  Look recursively from current directory.
  -h, --help       Show this help message and exit.
```




### Regex matching mode with custom written regex
`pvulnz -r -m -mr "REGEX"`  

### String matching mode with custom defined strings
`pvulnz -r -m -ms "STRING"`

### Functions recursive mode
`pvulnz -r`  

![Capture](https://user-images.githubusercontent.com/57464251/172067908-16967270-00f9-4ba1-b31e-9732a113ecf2.PNG)
