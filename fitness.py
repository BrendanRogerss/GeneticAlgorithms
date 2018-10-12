
problem = []

def numberPartition(bitString):
    sums = [0, 0]
    for i in range(len(problem)):
        sums[bitString[i]] += problem[i]
    return abs(sums[0] - sums[1])

def setCover(matrix):
    return 0
