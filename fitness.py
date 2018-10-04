problem = []

def setPartition(bitString):
    sums = [0, 0]
    for i in range(len(problem)):
        sums[bitString[i]] += problem[i]
    return abs(sums[0] - sums[1])
