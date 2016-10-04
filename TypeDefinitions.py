class POS(Enum):
    

class Node:
    wordTuple   # (word, pos) tuple, where word is the word as a string
                # and pos is the part of speech as an enum
                # in a graph, there should be at most one node with a given
                # (word, pos) tuple

    successorList # list of (node, probability) tuples, where probability is a
                  # float/number from 0 to 1

