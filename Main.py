import genotype
import fitness
import scanner
import LocalSearch.simulatedAnnealing as s
import LocalSearch.tabuSearch as t
import geneticAlgorithm as ga
import memeticAlgorithm as ma
import LocalSearch.hillClimbing as h
import timeit
import random
import glob

#problems = scanner.readNumberPartitioning('Data/NPInstances.dat')
problems = [scanner.readSetCover(file) for file in glob.glob("Data/SCP_Instances/Instances/*.txt")]
genotype.fitnessFunction = fitness.setCover


def randomSearch():
    solution = genotype.genotype()
    while solution.getFitness() != 0:
        solution = genotype.genotype()
        solution.setFitness()
        print(solution.bitString, solution.getFitness())


def simAneal():
    for i in problems:
        fitness.problem = i
        results = []
        for j in range(2):
            solution = s.run(genotype.genotype(), 120, s.tempDecay)
            results.append(solution.getFitness())
        with open("setCoverResults/SimulatedAnnealing.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)



def tabu():
    for i in problems:
        fitness.problem = i
        results = []
        for j in range(2):
            solution =t.run(genotype.genotype(), 15, 120)
            results.append(solution.getFitness())
        with open("setCoverResults/Tabu.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)



def memetic():

    for i in problems:
        fitness.problem = i
        results = []
        for j in range(2):
            solution =ma.memetic(120)
            results.append(solution.getFitness())
        with open("setCoverResults/memetic.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)

def genetic():

    for i in problems:
        fitness.problem = i
        results = []
        for j in range(2):
            print("starting new run")
            solution =ga.ga(120)
            results.append(solution.getFitness())
        with open("setCoverResults/genetic.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)

if __name__ == "__main__":
    #fitness.problem = problems[0]
    # bitStrings = [[random.randint(0,1) for i in range(200)] for i in range(1000)]
    start = timeit.default_timer()
    # for i in bitStrings:
    #     solution = genotype.genotype(i)
    # solution = s.run(genotype.genotype(), 5, s.tempDecay)
    # solution = h.run(solution, 1000, 1)
    # print(solution.getFitness(),fitness.isValid(solution), solution.getBitString())

    simAneal()

    stop = timeit.default_timer()
    print('Time: ', stop - start)