import numpy as np
problem = []

def numberPartition(bitString):
    sums = [0, 0]
    for i in range(len(problem)):
        sums[bitString[i]] += problem[i]
    return abs(sums[0] - sums[1])

def setCover(bitString):

    fitness = sum(problem[0][i] for i in np.where(bitString)[0])

    solution = np.logical_or.reduce([problem[i+1] for i in np.where(bitString)[0]])
    error = len(problem[1]) - np.count_nonzero(solution)


    fitness += error * problem[0][-1]
    return fitness


def isValid(genome):
    solution = np.logical_or.reduce([problem[i + 1] for i in np.where(genome.getBitString())[0]])
    error = len(problem[1]) - np.count_nonzero(solution)
    return error == 0