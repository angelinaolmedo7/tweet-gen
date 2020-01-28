import sys
import random


def rearrange(words):
    if (len(words) <= 1):
        # Received no parameters. First item will be name of file.
        return
    wordsList = words[1:]  # Just parameters
    random.shuffle(wordsList)
    return wordsList


if __name__ == '__main__':
    print(str(rearrange(sys.argv)))
