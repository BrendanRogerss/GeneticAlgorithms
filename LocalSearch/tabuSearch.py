import random
import genotype

def run(genome, tenure, iterations):
    tabu = [0 for i in range(len(genome.getBitString()))]

    for i in range(iterations):
        newBitString = genome.getBitString().copy()
        index = getViableIndex(tabu)
        newBitString[index] = not newBitString[index]
        newGenome = genotype.genotype(newBitString)
        newGenome.setFitness()
        if newGenome.getFitness() <= genome.getFitness():
            genome = newGenome
            updateTabu(tabu,tenure,index)
    return genome

def updateTabu(tabu, tenure, change):
    for i in range(len(tabu)):
        if tabu[i] != 0:
            tabu[i] -= tabu[i]
    tabu[change] = tenure
    return tabu

def getViableIndex(tabu):
    for i in range(10000):
        index = random.randint(0,len(tabu)-1)
        if tabu[index] == 0:
            return index
    print("No viable index")