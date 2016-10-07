from TypeDefinitions import Node, Sequence
from Utils import PosToInt
import Parser

import queue
from collections import deque
from heapq import *

def heuristic_generate(startingWord, sentenceSpec, graph):
    """Does the same thing as generate, but with the heuristic search strategy.

    Our heuristic function h(n) = n's current probability (n is a sequence)
    Nodes with a higher valued h(n) are preferred and are searched first
    """
    # much of the code is copied from generate()...
    nodeMap = Parser.parse(graph)

    sentenceSpecAsInts = [PosToInt(pos) for pos in sentenceSpec]

    startNode = nodeMap[(startingWord, sentenceSpecAsInts[0])]

    # ideally we use a heap/priority-queue to find the sequence with the highest
    # heuristic function value, but implementing that turned out to be difficult
    # Instead, we will just use a list to store the sequences to explore and
    # everytime we pick from the list, we find the one that has the highest
    # heuristic function value
    exploreStructure = []
    exploreStructure.append(Sequence(startNode))

    def heuristic_function(sequence):
        return sequence.probability

    exploreCount = 0
    currBestSentence = None
    while exploreStructure: # not empty
        # rather than checking for the goal state when popping from the 
        # explore data structure, we check before we're about to put it in,
        # to populate currBestSentence more quickly

        currSequence = max(exploreStructure, key=heuristic_function)
        exploreStructure.remove(currSequence)

        exploreCount += 1
        currNode = currSequence.nodes[-1]
        nextIdxInSentence = len(currSequence.nodes)
        nextPosAsInt = sentenceSpecAsInts[nextIdxInSentence]
        nextWordIsLast = (nextIdxInSentence == len(sentenceSpecAsInts) - 1)

        # sanity check
        if nextIdxInSentence > len(sentenceSpecAsInts) - 1:
            import pdb; pdb.set_trace()
            raise Exception("Unexpected! Goal state reached from currSequence!")

        for childNode, edgeProbability in currNode.successorList:
            if childNode.wordTuple[1] == nextPosAsInt:
                copiedSequence = currSequence.copy()
                copiedSequence.addNode(childNode, edgeProbability)

                # check if the resulting sequence has a chance at achieving better
                # probability
                if (not currBestSentence) or (copiedSequence.probability > currBestSentence.probability):
                    if nextWordIsLast:
                        currBestSentence = copiedSequence
                    else: # not nextWordIsLast
                        exploreStructure.append(copiedSequence)
          
    outputString = '"' + currBestSentence.getString() + '"' \
                   + " with probability " + str(currBestSentence.probability)
    print(outputString)
    print("Total nodes considered: ", exploreCount)

def generate(startingWord, sentenceSpec, graph, searchStrategy='BFS'):
    """Prints a string (not necessarily one line) with the following information:
    1. the highest-probability sentence found
    2. the number of nodes (i.e. word sequences) considerd during the search"""
    if searchStrategy=='heuristic':
        return heuristic_generate(startingWord, sentenceSpec, graph)

    nodeMap = Parser.parse(graph)

    sentenceSpecAsInts = [PosToInt(pos) for pos in sentenceSpec]

    startNode = nodeMap[(startingWord, sentenceSpecAsInts[0])]

    # represents sequences to explore, contains only sequences that currently
    # satisfy the sentenceSpec
    # depending on whether DFS or BFS is used, may use pop() or popleft() to
    # simulate stack or queue, respectively
    exploreStructure = deque()
    exploreStructure.append(Sequence(startNode))

    exploreCount = 0
    currBestSentence = None
    while exploreStructure: # not empty
        # rather than checking for the goal state when popping from the 
        # explore data structure, we check before we're about to put it in,
        # to populate currBestSentence more quickly
        
        if searchStrategy == 'BFS':
            currSequence = exploreStructure.popleft()
        elif searchStrategy == 'DFS':
            currSequence = exploreStructure.pop()
        exploreCount += 1
        currNode = currSequence.nodes[-1]
        nextIdxInSentence = len(currSequence.nodes)
        nextPosAsInt = sentenceSpecAsInts[nextIdxInSentence]
        nextWordIsLast = (nextIdxInSentence == len(sentenceSpecAsInts) - 1)

        # sanity check
        if nextIdxInSentence > len(sentenceSpecAsInts) - 1:
            import pdb; pdb.set_trace()
            raise Exception("Unexpected! Goal state reached from currSequence!")

        for childNode, edgeProbability in currNode.successorList:
            if childNode.wordTuple[1] == nextPosAsInt:
                copiedSequence = currSequence.copy()
                copiedSequence.addNode(childNode, edgeProbability)

                # check if the resulting sequence has a chance at achieving better
                # probability
                if (not currBestSentence) or (copiedSequence.probability > currBestSentence.probability):
                    if nextWordIsLast:
                        currBestSentence = copiedSequence
                    else: # not nextWordIsLast
                        exploreStructure.append(copiedSequence)
          
    outputString = '"' + currBestSentence.getString() + '"' \
                   + " with probability " + str(currBestSentence.probability)
    print(outputString)
    print("Total nodes considered: ", exploreCount)

# kind of like the main function to run for test results
def test(filename="input.txt"):
    file = open(filename, "r")
    text = file.read()

    def sentenceSpecToString(sentenceSpec):
        string = "'" + sentenceSpec[0] + "'"
        for spec in sentenceSpec[1:]:
            string += ", '" + spec + "'"
        return string

    searchStrategy = 'heuristic'

    print("====================================")
    sentenceSpec = ['NNP', 'VBD', 'DT', 'NN']
    startingWord = 'hans'
    print("output for starting word: ", startingWord, "\nand specs:", sentenceSpecToString(sentenceSpec))
    generate(startingWord, sentenceSpec, text, searchStrategy)

    # part 2 tests:
    print("====================================")
    sentenceSpec = ['NNP', 'VBD', 'DT', 'NN']
    startingWord = 'benjamin'
    print("output for starting word: ", startingWord, "\nand specs:", sentenceSpecToString(sentenceSpec))
    generate(startingWord, sentenceSpec, text, searchStrategy)

    print("====================================")
    sentenceSpec = ['DT', 'NN', 'VBD', 'NNP']
    startingWord = 'a'
    print("output for starting word: ", startingWord, "\nand specs:", sentenceSpecToString(sentenceSpec))
    generate(startingWord, sentenceSpec, text, searchStrategy)

    print("====================================")
    sentenceSpec = ['NNP', 'VBD', 'DT', 'JJS', 'NN']
    startingWord = 'benjamin'
    print("output for starting word: ", startingWord, "\nand specs:", sentenceSpecToString(sentenceSpec))
    generate(startingWord, sentenceSpec, text, searchStrategy)

    print("====================================")
    sentenceSpec = ['DT', 'NN', 'VBD', 'NNP', 'IN', 'DT', 'NN']
    startingWord = 'a'
    print("output for starting word: ", startingWord, "\nand specs:", sentenceSpecToString(sentenceSpec))
    generate(startingWord, sentenceSpec, text, searchStrategy)
