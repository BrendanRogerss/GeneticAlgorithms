import genotype
import fitness
import scanner
import LocalSearch.simulatedAnnealing as s
import LocalSearch.tabuSearch as t
import geneticAlgorithm as ga
import memeticAlgorithm as ma
import LocalSearch.hillClimbing as h

#problems = scanner.readNumberPartitioning('Data/NPInstances.dat')
problems = scanner.readSetCover("Data/SCP_Instances/Instances/scp41.txt")
genotype.fitnessFunction = fitness.setCover
# decreased size in genotype by 1


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
        for j in range(5):
            solution = s.run(genotype.genotype(), 100000, s.tempDecay)
            results.append(solution.getFitness())
        with open("results/SimulatedAnnealing2.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)



def tabu():
    for i in problems:
        fitness.problem = i
        results = []
        for j in range(5):
            solution =t.run(genotype.genotype(), 15, 100000)
            results.append(solution.getFitness())
        with open("results/Tabu.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)



def memetic():

    for i in problems:
        fitness.problem = i
        results = []
        for j in range(5):
            solution =ma.memetic(20)
            results.append(solution.getFitness())
        with open("results/memetic.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)

def genetic():

    for i in problems[0]:
        fitness.problem = i
        results = []
        for j in range(5):
            solution =ga.ga(200)
            results.append(solution.getFitness())
        with open("results/genetic.txt", 'a') as myfile:
            output = str(min(results))+" "+str((sum(results)/len(results)))+" "+str(max(results))+"\n"
            myfile.write(output)

if __name__ == "__main__":
    fitness.problem = problems
    print(len(problems))
    solution =ga.ga(200)
    print(solution.getFitness(), solution.getBitString())
