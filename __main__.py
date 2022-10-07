#Example Code
#source activate py10
#python3 /Users/sub01/Documents/Codes/Pythonic_TI-Basic_Compiler/ -c /Users/sub01/Documents/Test_Codes/Example1.py

# Importing global modules
import argparse
import os
import sys

# Inserting modules to system path
if "/" in str(os.getcwd()):
    sys.path.insert(0, f"{os.getcwd()}/Pythonic_TI-Basic_Compiler/scripts")
if "\\" in str(os.getcwd()):
    sys.path.insert(0, f"{os.getcwd()}\\Pythonic_TI-Basic_Compiler\\scripts")
# Importing local modules from ./scripts
from scripts import setup, fileInfo, translate

# Initiating startup and checking supported OS
platform = setup.platform()


class parse:
    def read(args):
        argList = [str(args.read[n]) for n in len(args)]
        return argList


def main():
    # Create Parser Object
    parser = argparse.ArgumentParser(description="Compiler for TI-Basic code from Python")

    # Defining arguments for the parser object
    parser.add_argument("-c", "--compile", metavar="fileName", type=str, nargs=1, default=None,
                        help="Compiles .py scripts to .XP file")

    # parse the arguments from standard input
    args = parser.parse_args()
    if args.compile != None:
        filePath = str(args.compile[0])
        validation = fileInfo.validate(filePath)
        if validation and ".py" in str(filePath):
            file, parentPath = fileInfo.pathInfo(filePath, parentCond=True)
            translate.compiler.read(filePath)
        else:
            print("File not a python file!")
            exit()


if __name__ == "__main__":
    main()
