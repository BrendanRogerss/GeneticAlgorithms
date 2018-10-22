import numpy as np
problem = []

def numberPartition(bitString):
    sums = [0, 0]
    for i in range(len(problem)):
        sums[bitString[i]] += problem[i]
    return abs(sums[0] - sums[1])

def setCover(bitString):

    # solution = [i for i in range(len(bitString))]
    # for i in range(len(bitString)):
    #     if bitString[i]==1:
    #         currentSet = problem[i+1]
    #         for j in solution:
    #             if currentSet[j] == 1:
    #                 solution.remove(j)

    solution = np.zeros((1,len(problem[1])))[0]
    for i in range(len(bitString)):
        if bitString[i]==1:
            print(len(solution))
            print(len(problem[i+1]))
            solution = np.bitwise_or(solution,problem[i+1])
    error = np.count_nonzero(solution, arr=0)

    fitness = sum(problem[0][i] for i in np.where(bitString)[0])
    fitness += len(error) * problem[0][-1]
    return fitness
