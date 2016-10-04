from TypeDefinitions import Node
from Utils import PosToInt

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

