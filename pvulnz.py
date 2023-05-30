#!/usr/bin/env python3

import os
import argparse
import sys
import re
from signal import signal, SIGPIPE, SIG_DFL
from pathlib import Path

signal(SIGPIPE, SIG_DFL)

scriptPath = os.path.dirname(os.path.realpath(__file__))
functionFile = scriptPath + os.sep + "functions.txt"
def modifyFunctions(line, mode):
    if(not os.access(functionFile, os.W_OK)):
        print("File: '" + functionFile + "' is not writeable. Exiting...")
        sys.exit(-1)

    if(mode == "add"):
        with open(functionFile, "a") as f:
            f.write(args.add + "\n")
    elif(mode == "delete"):
        with open(functionFile, "r") as f:
            lines = f.readlines()

        with open(functionFile, "w") as f:
            for line in lines:
                if(line.strip() != args.delete):
                    f.write(line)
    else: exit

def main():
    if(args.add): 
        modifyFunctions(args.add, "add")
        print("[i] Added '" + args.add + "' function to 'functions.txt' file")

    elif(args.delete): 
        modifyFunctions(args.delete, "delete")
        print("[i] Deleted '" + args.delete + "' function from 'functions.txt' file")
    
    #Get script's location path

    with open(scriptPath + os.sep + "functions.txt", "r", errors="ignore") as functionsFile:
        functionLines = [i.strip() for i in functionsFile]
        
        filesToLook = []
        
        for f in files:
            if(not os.path.exists(f)):
                print("[!] File '" + str(f) + "' doesn't exist. Skipping...")
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
                if(".php" not in str(path) or not str(path).endswith(".php")):
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

                        #Match string
                        if(args.match_string):
                            if(args.match_string in j): 
                                print("[MS] " + str(path) + ":" + str(count) + "\t" + j)

                        # Match regex
                        if(args.match_regex):
                            if(re.search(args.match_regex, j)):
                                print("[MR] " + str(path) + ":" + str(count) + "\t" + j)
                        
                        # If match mode is activated, exit
                        if(args.match):
                            continue

                        #Check if dangerous function is used with a variable
                        if(i in j and "$" in j):
                            try:
                                print(str(path) + ":" + str(count) + "\t" + j)
                            except UnicodeDecodeError:
                                pass
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pvulnz, PHP static analysis helper tool", add_help=False)
    parser.add_argument("files", type=str, metavar="file(s)", nargs = "*", help="\t\t Specify php file(s) to look at, '*' for all.")
    parser.add_argument("-a", metavar="<function>", dest="add", help="\t\t Specify function name to add to the functions file")
    parser.add_argument("-d", metavar="<function>", dest="delete", help="\t\t Specify function name to delete from the functions file")
    parser.add_argument("-m", action = "store_true", dest="match", help="\t\t Turn on match mode, while in this mode, 'functions.txt' is ignored")
    parser.add_argument("-ms", metavar="<string>", dest="match_string", help="\t\t Specify string to match from parsed files.")
    parser.add_argument("-mr", metavar="<regex>", dest="match_regex", help="\t\t Specify regex string to match from parsed files.")
    parser.add_argument("-r", "--recursive", action = "store_true", dest="recurse", help="\t\t Look recursively from current directory.")
    parser.add_argument('-h', '--help', action="help", default=argparse.SUPPRESS, help='\t\t Show this help message and exit.') 
    args = parser.parse_args()
    
    files = args.files

    main()
