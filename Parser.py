import Utils;
from TypeDefinitions import Node;

# 
# file = open("input.txt", "r");
# 

        
def parse(graph):
    """Returns a map of (word, posAsInt) to node, given graph,
    which is the string/text of the entire input.txt"""
    lookUp = dict();

    def addNodeToLookUpIfNotExist(word, posAsInt):
        if (word, posAsInt) not in lookUp:
            lookUp[(word, posAsInt)] = Node(word, posAsInt);
        return lookUp[(word, posAsInt)]

    splitText = graph.split("\n"); 
    for line in splitText:
        splitLine = line.split("/");
        firstWord = splitLine[0];
        firstPos = Utils.PosToInt(splitLine[1]);
        firstNode = addNodeToLookUpIfNotExist(firstWord, firstPos);
        secondWord = splitLine[3];
        secPos = Utils.PosToInt(splitLine[4]);
        secondNode = addNodeToLookUpIfNotExist(secondWord, secPos);
        # now nodes are already created for this line, if required
        probability = float(splitLine[6]);
        firstNode.successorList.append((secondNode, probability))

    return lookUp;
