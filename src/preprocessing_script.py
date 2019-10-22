import sys
import string

from stringoperations import *

fileName_pattern = "arquivodeentrada.txt"

def getFileName():
    if len(sys.argv)>=1:
        return sys.argv[1]
    else:
        return fileName_pattern

def openFile(fileName):
    file = open(fileName)
    return file

def applyFuncByLine(f, func):
    lines = f.readlines()

    for line in lines:
        print(func(line))
        x = input()

def main():
    fileName = getFileName()
    file = openFile(fileName)

    applyFuncByLine(file, removewhitespaces)

if __name__ == '__main__':
    main()