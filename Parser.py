import Utils;
from TypeDefinitions import Node;

# 
# file = open("input.txt", "r");
# 


graph = """there/EX//was/VBD//0.21311475409836064
there/EX//still/RB//0.03278688524590164
there/EX//could/MD//0.01639344262295082
there/EX//nailed/VBD//0.01639344262295082
there/EX//they/PRP//0.03278688524590164
there/EX//were/VBD//0.08196721311475409
there/EX//is/VBZ//0.22950819672131148
there/EX//no/DT//0.03278688524590164
there/EX//spring/NN//0.01639344262295082
there/EX//are/VBP//0.04918032786885246
there/EX//must/MD//0.01639344262295082
there/EX//came/VBD//0.01639344262295082
there/EX//appeared/VBD//0.01639344262295082
there/EX//some/DT//0.01639344262295082
there/EX//you/PRP//0.01639344262295082
there/EX//joined/VBD//0.01639344262295082
there/EX//stood/VBD//0.01639344262295082
there/EX//he/PRP//0.06557377049180328
there/EX//arose/VBD//0.01639344262295082
there/EX//the/DT//0.01639344262295082
there/EX//time/NN//0.01639344262295082
there/EX//as/IN//0.01639344262295082
there/EX//lived/VBD//0.01639344262295082
there/EX//lay/VBD//0.01639344262295082
was/VBD//mourning/VBG//0.0035714285714285713
was/VBD//about/IN//0.007142857142857143
was/VBD//the/DT//0.04642857142857143
was/VBD//a/DT//0.06428571428571428
was/VBD//bowed/VBN//0.0035714285714285713
was/VBD//dead/JJ//0.007142857142857143
was/VBD//so/RB//0.04285714285714286
was/VBD//but/CC//0.0035714285714285713
was/VBD//ended/VBN//0.0035714285714285713
was/VBD//carried/VBN//0.014285714285714285
was/VBD//necessary/JJ//0.0035714285714285713
was/VBD//listening/VBG//0.0035714285714285713
was/VBD//still/RB//0.007142857142857143
was/VBD//in/IN//0.03214285714285714
was/VBD//stern/JJ//0.0035714285714285713
was/VBD//gradually/RB//0.0035714285714285713
was/VBD//as/IN//0.014285714285714285
was/VBD//removed/VBN//0.0035714285714285713
was/VBD//twilight/NN//0.0035714285714285713
was/VBD//pressed/VBN//0.0035714285714285713
was/VBD//inaudible/JJ//0.0035714285714285713
was/VBD//to/TO//0.039285714285714285
was/VBD//called/VBN//0.0035714285714285713
was/VBD//borne/VBN//0.0035714285714285713
was/VBD//lighted/VBN//0.0035714285714285713"""

        
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

        import pdb; pdb.set_trace();
        print(line);
 

