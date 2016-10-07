import copy

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

class Sequence:
    def __init__(self, startNode):
        self.nodes = [startNode]
        self.probability = 1

    def addNode(self, node, edgeProbability):
        self.nodes.append(node)
        self.probability *= edgeProbability

    def copy(self):
        """Returns a copy of self, with a copied list pointing to the
        same Nodes"""
        theCopy = Sequence(None) # use a temporary startNode
        theCopy.nodes = copy.copy(self.nodes)
        theCopy.probability = self.probability
        return theCopy

    def getString(self):
        string = ""
        first = True
        for node in self.nodes:
            if first:
                first = False
            else:
                string += " "
            string += node.wordTuple[0]

        return string
