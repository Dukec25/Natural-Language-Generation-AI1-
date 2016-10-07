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

