class Node:
    def __init__(self, word, posAsInt):
        # (word, pos) tuple, where word is the word as a string
        # and pos is the part of speech as an int (see Utils.PosToInt)
        # in a graph, there should be at most one node with a given
        # (word, pos) tuple
        self.wordTuple = (word, posAsInt)

        # list of (node, probability) tuples, where probability 
        # is a float/number from 0 to 1
        self.successorList = []
