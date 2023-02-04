# pvulnz

PHP static analysis tool.

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
usage: pvulnz.py [-r] [-h] [files ...]

pvulnz, tool for finding dangerous lines in PHP code.

positional arguments:
  file(s)          Specify php file(s) to look at, '*' for all.

optional arguments:
  -r, --recursive  Look recursively from current directory.
  -h, --help       Show this help message and exit.
```

## Example
`pvulnz -r`  

![Capture](https://user-images.githubusercontent.com/57464251/172067908-16967270-00f9-4ba1-b31e-9732a113ecf2.PNG)
