from TypeDefinitions import Node, Sequence
from Utils import PosToInt
import Parser

import operator
import queue

def generate(startingWord, sentenceSpec, graph):
    """Returns a string (not necessarily one line) with the following information:
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
                
    return currBestSentence # TODO testing, return string later?

def test(filename="input.txt"):
    file = open(filename, "r")
    text = file.read()
    sentenceSpec1 = ['NNP', 'VBD', 'DT', 'NN']
    return generate('hans', sentenceSpec1, text)


def getKey(item):
    return item[1];

""" untested 
# always choose the word of right type of POS and have the highest possibility
def heuristic(startNode, sentenceSpec, graph):
    index = 1; # current word 
    "sort the list so highest probabilities goes first"
    result = [];
    result.append(startNode.wordTuple[0]);
    probability = 1;
    currentNode = startNode;
    success = False; 

    while( currentNode != None ) 
        sorted(startNode.successorList, key=getKey, reverse=true); 
        for pairedElement in startNode.successorList:
            if pairedElement.wordTuple[1] == sentenceSpec[index]:
                    if (index == len(sentenceSpec) -1):
                        success = True;
                        currentNode = None;
                        break; 
                    index = index + 1;
                    result.append(" " + pairedElement.wordTuple[0]);
                    probability = probability * currentNode.successorList[1];
                    currentNode = pairedElement; 
                    continue;
        break; 

    if (success):
        #print out stuff
    else
        #print out stuff 
"""

