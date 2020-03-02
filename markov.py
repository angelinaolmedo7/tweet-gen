from dictogram import Dictogram
import random
from numpy.random import choice


class MarkovChain:

    def __init__(self, word_list):
        # The Markov chain will be a dictionary of dictionaries
        # Example: for "one fish two fish red fish blue fish"
        # {"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two":
        # {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            # get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys():  # already there
                # get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                # add to count
                histogram[next_word] = histogram.get(next_word, 0) + 1
            else:  # first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = [random.choice(list(self.markov_chain.keys()))]
        print(sentence[0])
        for i in range(1, num_words):
            probability_dict = self.markov_chain[sentence[i-1]]
            print("Probabilities for target word " + sentence[i-1] + ": ")
            print(probability_dict)

            prob_list = []
            num_words = 0
            for num in list(probability_dict.values()):
                num_words += num

            for num in list(probability_dict.values()):
                prob_list.append(num / num_words)

            print(prob_list)

            print(list(probability_dict.keys()))
            print(list(probability_dict.values()))

            # print(choice(list(probability_dict.keys()), 1, p=list(probability_dict.values()))[0])

            sentence.append(choice(list(probability_dict.keys()), 1, p=prob_list)[0])
            print(sentence)

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)


markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish", "fish", "two", "fish"])
markov_chain.walk(5)
# markov_chain.print_chain()
# print(markov_chain.walk(10))
