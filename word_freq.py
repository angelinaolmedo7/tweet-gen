import sys
import random
import string


def histogram(fileName):
    textFile = open(fileName, "r")
    fileLines = textFile.readlines()
    histogram = {}

    for line in fileLines:
        for word in line.split():
            # strip punctuation/capitals
            i = word.lower().translate(
                str.maketrans('', '', string.punctuation))
            if i in histogram:
                histogram[i] = histogram[i] + 1
            else:
                histogram[i] = 1

    return histogram


def unique_words(fileName):
    return len(histogram(fileName))


def frequency(fileName, target):
    return histogram(fileName)[target]


if __name__ == '__main__':
    print(histogram(str(sys.argv[1])))
    print(unique_words(str(sys.argv[1])))
    print(frequency(str(sys.argv[1]), str(sys.argv[2])))
