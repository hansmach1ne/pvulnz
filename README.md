# pvulnz
PHP source code vulnerability scanner/dangerous function echoing tool.

It will print out 'dangerous' lines with functions defined inside 'functions.txt'.


## -h, --help
```
usage: vulnz.py [-r] [-e <extension>] [-h] [files ...]

pvulnz, PHP source code vulnerability scanner/dangerous function echoing tool

positional arguments:
  file(s)          Specify php file(s) to look at, '*' for all.

optional arguments:
  -r, --recursive  Look recursively from current directory.
  -e <extension>   Specify what file extension to look at.
  -h, --help       Show this help message and exit.
```
