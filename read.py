import linecache
from os import closerange


def readFullLine(filepath, startNum):
    lineNum = startNum
    line = ""
    while True:
        line = line + linecache.getline(filepath, lineNum)
        lineNum = lineNum + 1
        if ")" in line:
            break
    return line


def tabLineToList(line, leadingSpace=False):
    splitText = " , " if leadingSpace else ", "
    start = line.index("(")
    end = line.index(")")
    return line[start + 2 : end].split(splitText)


def getColumnIndices(*args, filepath="CO2.tab"):
    """
    Returns the indices of the specified columns
    """
    # idxDict = {"PT": 0, "TM": 0, "HG": 0, "SEG": 0}
    idxDict = {"PT": 0, "TM": 0, "HG": 0}
    if filepath:
        cols = tabLineToList(readFullLine(filepath, 52))
    for key in idxDict:
        idxDict[key] = cols.index(key)
    return idxDict


def outputList(l, file):
    file.write(",".join(l) + "\n")


with open("CO2.tab") as f:
    cols = getColumnIndices()
    print(f"\nCOLUMNS:\n{cols}\n")

    with open("out.csv", "w") as out:
        outputList([k for k in cols.keys()], out)

        for line in f.readlines()[52:]:
            l = tabLineToList(line)
            vals = [l[i].strip() for i in cols.values()]
            print(vals)
            outputList(vals, out)

