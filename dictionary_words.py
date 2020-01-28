import sys
import random


def randomWords(num):
    dictionary = open("/usr/share/dict/words", "r")
    dictLines = dictionary.readlines()
    wordsList = []

    for i in range(0, num):
        wordsList.append(random.choice(dictLines).rstrip('\n'))
    return wordsList


if __name__ == '__main__':
    print(randomWords(int(sys.argv[1])))
