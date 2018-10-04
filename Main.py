import genotype
import fitness
import scanner
import LocalSearch.hillClimbing as h


problem = scanner.readSetPartitioning('SetProblems/NPInstances.dat')[0]
#problem = scanner.readShittySetPartitioning("SetProblems/a.csv")
fitness.problem = problem
genotype.fitnessFunction = fitness.setPartition


def randomSearch():
    solution = genotype.genotype()
    while solution.getFitness() != 0:
        solution = genotype.genotype()
        solution.generateBitstring(len(problem))
        solution.setFitness()
        print(solution.bitString, solution.getFitness())

def hillSearch():
    solution = genotype.genotype()
    solution.generateBitstring(len(problem))
    while True:
        solution = h.run(solution,10000, 0.1)
        print(solution.fitness)


hillSearch()
