# pvulnz
PHP source code vulnerability scanner/dangerous function echoing tool.

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
usage: vulnz.py [-r] [-h] [files ...]

pvulnz, PHP source code vulnerability scanner/dangerous function echoing tool

positional arguments:
  file(s)          Specify php file(s) to look at, '*' for all.

optional arguments:
  -r, --recursive  Look recursively from current directory.
  -h, --help       Show this help message and exit.
```
