from TypeDefinitions import Node
from Utils import PosToInt

import operator
import queue

def generate(startingWord, sentenceSpec, graph):
    """Returns a string (not necessarily one line) with the following information:
    1. the highest-probability sentence found
    2. the number of nodes (i.e. word sequences) considerd during the search"""
    nodeMap = parse(graph)

    sentenceSpecAsInts = [PosToInt(pos) for pos in sentenceSpec]

    startNode = nodeMap[(startingWord, sentenceSpecAsInts[0])]

    # represents nodes to explore
    # each element is a tuple of form (node, idx, )
    # - idx: index used in sentenceSpec 
    exploreQueue = queue.Queue()    
    exploreQueue.put_nowait(startNode)

    while not exploreQueue.empty():
        currNode = exploreQueue.get_nowait()


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

