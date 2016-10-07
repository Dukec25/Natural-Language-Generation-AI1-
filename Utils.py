posToIntMap = {
    "CC" : 1,
    "CD" : 2,
    "DT" : 3,
    "EX" : 4,
    "FW" : 5,
    "IN" : 6,
    "JJ" : 7,
    "JJR" : 8,
    "JJS" : 9,
    "LS" : 10,
    "MD" : 11,
    "NN" : 12,
    "NNS" : 13,
    "NNP" : 14,
    "NNPS" : 15,
    "PDT" : 16,
    "POS" : 17,
    "PRP" : 18,
    "PRP$" : 19,
    "RB" : 20,
    "RBR" : 21,
    "RBS" : 22,
    "RP" : 23,
    "TO" : 24,
    "UH" : 25,
    "VB" : 26,
    "VBD" : 27,
    "VBG" : 28,
    "VBN" : 29,
    "VBP" : 30,
    "VBZ" : 31,
    "WDT" : 32,
    "WP" : 33,
    "WP$" : 34,
    "WRB" : 35,
    # additional ones not found in http://www.winwaed.com/blog/2011/11/08/part-of-speech-tags/
    "SYM" : 36,
    "-LRB-" : 37,
    "-RRB-" : 38,
}

def PosToInt(pos):
    """Returns an integer represenation for the given pos"""
    if pos not in posToIntMap:
        raise Exception("Unrecognized part of word: " + pos)
    return posToIntMap[pos]

# function to extract POS's from the input file. Buggy? Might not need?
def extract():
    file = open("input.txt", "r")
    text = file.read()
    splitText = graph.split("\n")

    posSet = set()
    for line in splitText:
        splitLine = line.split("/");
        firstPos = splitLine[1];
        posSet.add(firstPos)
        secondPos = splitLine[4]
        posSet.add(secondPos)

    for pos in posSet:
        print(pos)
