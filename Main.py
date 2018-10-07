import genotype
import fitness
import scanner
import LocalSearch.hillClimbing as h
import LocalSearch.simulatedAnnealing as s
import LocalSearch.tabuSearch as t
import  LocalSearch.bestNeighbour as b


problem = scanner.readSetPartitioning('SetProblems/NPInstances.dat')[0]
# problem = scanner.readShittySetPartitioning("SetProblems/a.csv")
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
        #print(solution == b.run(solution))

def simAneal():
    solution = genotype.genotype()
    solution.generateBitstring(len(problem))
    while True:
        solution = s.run(solution, 10000, s.tempDecay)
        #print(solution.getBitString(),solution.fitness)


def tabu():
    solution = genotype.genotype()
    solution.generateBitstring(len(problem))
    for i in range(100):
        solution = t.run(solution, 3, 100)
        #print(solution.getBitString(),solution.fitness)
    print(solution == b.run(solution))


simAneal()
