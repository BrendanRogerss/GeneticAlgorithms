import genotype
import fitness
import scanner
import LocalSearch.hillClimbing as h
import LocalSearch.simulatedAnnealing as s
import LocalSearch.tabuSearch as t
import LocalSearch.bestNeighbour as b
from population import generatePop, sort
import geneticAlgorithm as ga
import memeticAlgorithm as ma


problem = scanner.readSetPartitioning('SetProblems/NPInstances.dat')[0]
# problem = scanner.readShittySetPartitioning("SetProblems/a.csv")
fitness.problem = problem
genotype.fitnessFunction = fitness.setPartition


def randomSearch():
    solution = genotype.genotype()
    while solution.getFitness() != 0:
        solution = genotype.genotype()
        solution.setFitness()
        print(solution.bitString, solution.getFitness())

def hillSearch():
    solution = genotype.genotype()
    while True:
        solution = h.run(solution,10000, 0.1)
        print(solution.fitness)
        #print(solution == b.run(solution))

def simAneal():
    solution = genotype.genotype()
    while True:
        solution = s.run(solution, 10000, s.tempDecay)
        #print(solution.getBitString(),solution.fitness)


def tabu():
    solution = genotype.genotype()
    for i in range(100):
        solution = t.run(solution, 3, 100)
        #print(solution.getBitString(),solution.fitness)
    print(solution == b.run(solution))


if __name__ == "__main__":

    # pop = generatePop(100000)
    # pop = sort(pop)
    # #for i in pop:
    # #    print(i.getFitness())
    # print(pop[0].getBitString(), pop[0].getFitness())
    solution = ma.ga(100)
    print(solution.getBitString(), solution.getFitness())
