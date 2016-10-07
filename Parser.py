import Utils;
from TypeDefinitions import Node;

# 
# file = open("input.txt", "r");
# 

        
def parse(graph):
    """Returns a map of (word, posAsInt) to node, given graph,
    which is the string/text of the entire input.txt"""
    lookUp = dict();
    splitText = graph.split("\n"); 
    for line in splitText:
        splitLine = line.split("/");
        firstWord = splitLine[0];
        pos = Utils.PosToInt(splitLine[1]);
        secondWord = splitLine[3];
        secPos = Utils.PosToInt(splitLine[4]);
        probability = splitLine[6][0:-1];
        node = Node(firstWord, pos);
        """if the node already existed, just append to its list; 
        otherwise create the node, and append to its list"""
        if (secondWord, secPos) not in lookUp:
            lookUp[(secondWord, secPos)] = node;
            node.successorList.append((Node(secondWord, secPos), probability));
        else:
            lookUp[(secondWord, secPos)].successorList.append((Node(secondWord, 
                            secPos), probability));

        print(line);
    return lookUp;
 

