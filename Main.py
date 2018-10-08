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


problems = scanner.readSetPartitioning('SetProblems/NPInstances.dat')
# problem = scanner.readShittySetPartitioning("SetProblems/a.csv")
#fitness.problem = problem
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
    for i in range(100):
        solution = genotype.genotype()
        solution = t.run(solution, 3, 1000)
        print(solution.getBitString(),solution.fitness)
    #print(solution == b.run(solution))


def memetic():
    for i in problems:
        fitness.problem = i
        solution = ma.ga(200)
        with open("results.txt", "a") as myfile:
            output = str(solution.getBitString())+" "+str(solution.getFitness())+"\n"
            print(output)
            myfile.write(output)


if __name__ == "__main__":

    for i in problems[:5]:
        fitness.problem = i
        # tabu()
        best = b.bruteForce()
        print(best.getBitString(), best.getFitness())