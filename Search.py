from TypeDefinitions import Node, Sequence
from Utils import PosToInt
import Parser

import operator
import queue

def generate(startingWord, sentenceSpec, graph):
    """Prints a string (not necessarily one line) with the following information:
    1. the highest-probability sentence found
    2. the number of nodes (i.e. word sequences) considerd during the search"""
    nodeMap = Parser.parse(graph)

    sentenceSpecAsInts = [PosToInt(pos) for pos in sentenceSpec]

    startNode = nodeMap[(startingWord, sentenceSpecAsInts[0])]

    # represents sequences to explore, contains only sequences that currently
    # satisfy the sentenceSpec
    exploreQueue = queue.Queue()    
    exploreQueue.put_nowait(Sequence(startNode))

    exploreCount = 0
    currBestSentence = None
    while not exploreQueue.empty():
        # rather than checking for the goal state when popping from the 
        # explore data structure, we check before we're about to put it in,
        # to populate currBestSentence more quickly
        currSequence = exploreQueue.get_nowait()
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
                        exploreQueue.put_nowait(copiedSequence)
          
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
            string = ", '" + spec + "'"
        return string

    print("====================================")
    sentenceSpec1 = ['NNP', 'VBD', 'DT', 'NN']
    startingWord1 = 'hans'
    print("output for starting word: ", startingWord1, sentenceSpecToString(sentenceSpec1))
    generate(startingWord1, sentenceSpec1, text)
