import numpy as np
problem = []

def numberPartition(bitString):
    sums = [0, 0]
    for i in range(len(problem)):
        sums[bitString[i]] += problem[i]
    return abs(sums[0] - sums[1])

def setCover(bitString):
    # print("A")
    # solution = [i for i in range(len(bitString))]
    # for i in range(len(bitString)):
    #     if bitString[i]==1:
    #         currentSet = problem[i+1]
    #         for j in solution:
    #             if currentSet[j] == 1:
    #                 solution.remove(j)
    fitness = sum(problem[0][i] for i in np.where(bitString)[0])
    solution = np.zeros((1,len(problem[1])), dtype=np.int64)[0]
    solution = [np.bitwise_or(solution, problem[i+1], out=solution) for i in np.where(bitString)[0]][0]
    # solution = np.bitwise_or(solution, [problem[i+1]for i in np.where(bitString)[0]])
    # print(np.count_nonzero(solution[0]), np.count_nonzero(solution[-1]))
    error = len(problem[1]) - np.count_nonzero(solution[0])
    # print(len(problem[1]), np.count_nonzero(solution))
    # if error > 0 :
    #     #fitness = float('inf')
    #     print("genome not valid. Error:", error)


    fitness += error * problem[0][-1]
    return fitness


def isValid(genome):
 return 0