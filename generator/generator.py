#!/usr/bin/python

__author__ = "Matan Lachmish"
__copyright__ = "Copyright 2016"
__version__ = "1.2"
__status__ = "Development"

import sys
import random
import string

def main(argv=sys.argv):
    # Usage check
    if 3 != len(argv):
        print "Usage: python %s [localizable source file] [output file]" % argv[0]
        return -1

    print ''
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '~~~ Welcome to gibrrish - localization tester for iOS ~~~'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print ''

    print 'Preparing localizable file',
    try:
        inputFileName = argv[1];
        inputFile = open(inputFileName, 'r')
    except IOError:
        print 'Cannot open ' + inputFileName
        return -1

    try:
        outputFileName = argv[2];
        outputFile = open(outputFileName, 'w')
    except IOError:
        print 'Cannot open ' + outputFile
        return -1

    printDone()

    inputLines = inputFile.readlines()
    for inputLine in inputLines:
        line_split = inputLine.split('=')
        if len(line_split) == 2:
            newString = ''.join(random.choice(string.ascii_letters + string.octdigits + ' ?!:+-') for _ in range(2*len(line_split[1])))
            line_split[1] = '"' + newString + '";\n';
        outputFile.write('='.join(line_split))

    inputFile.close()
    outputFile.close()

    return 0


def printDone():
    print '... Done'

def printProgress(percentage):
    sys.stdout.write("\r%d%%" % percentage)
    sys.stdout.flush()
