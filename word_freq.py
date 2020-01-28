import sys
import random


def getHist(fileName):
    textFile = open(fileName, "r")
    fileLines = textFile.readlines()
    histogram = {}

    for line in fileLines:
        for word in line.split():
            i = word.lower()
            if i in histogram:
                histogram[i] = histogram[i] + 1
            else:
                histogram[i] = 1

    return histogram


if __name__ == '__main__':
    print(getHist(str(sys.argv[1])))
