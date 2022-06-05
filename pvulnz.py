#!/usr/bin/env python3

import os
import argparse
from signal import signal, SIGPIPE, SIG_DFL
from pathlib import Path

signal(SIGPIPE, SIG_DFL)

def main():
    
    with open("/home/kali/Private/vulnz/functions.txt", "r", errors="ignore") as functionsFile:
        functionLines = [i.strip() for i in functionsFile]
        
        filesToLook = []
        
        for f in files:
            if(not os.path.exists(f)):
                print("File '" + str(f) + "' doesn't exist. Skipping...")
                continue
            #Check if * is supplied, if it is scan entire current directory
            elif(str(f) == "*"):
                filesToLook = os.listdir()
                break
            
            #File supplied exists, adding it to array
            else: 
                filesToLook.append(f)

        #If recursive option is supplied ('-r' or '--recursive')
        if(args.recurse or len(filesToLook) == 0):
            filesToLook = list(Path(".").rglob("*"))
        
        for path in filesToLook:
       
            #If not a file, skip
            if(os.path.isdir(path)):
                continue
            else:
                if(".php" not in str(path)):
                    continue
                #Loop through each file in a current directory
                with open(path, "r", encoding = "utf-8", errors="ignore") as f:
                    fileLines = [i.strip() for i in f]
            
                #Loop through all dangerous functions in wordlist
                for i in functionLines:
                     #Loop through each line of the file
                    count = 0
                    for j in fileLines:
                        count = count + 1
                        #Check if dangerous function is used with a variable
                        if(i in j and "$" in j):
                            try:
                                print(str(path) + ":" + str(count) + "\t" + j)
                            except UnicodeDecodeError:
                                pass
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="vulnz, Mach1ne's tool for finding php source code vulns.", add_help=False)
    parser.add_argument("files", type=str, metavar="file(s)", nargs = "*", help="\t\t Specify php file(s) to look at, '*' for all.")
    parser.add_argument("-r", "--recursive", action = "store_true", dest="recurse", help="\t\t Look recursively from current directory.")
    parser.add_argument('-h', '--help', action="help", default=argparse.SUPPRESS, help='\t\t Show this help message and exit.') 
    args = parser.parse_args()
    
    files = args.files

    main()
