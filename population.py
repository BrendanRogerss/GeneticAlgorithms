import genotype
import random


def generatePop(popSize):
    # randomly generate population
    pop = []
    for i in range(popSize):
        pop.append(genotype.genotype())
    return pop


def randomSample(population, sampleSize):
    # dont think i actually use this....
    if population < sampleSize:
        assert "population less than sample size"
    indexes = set()
    while len(indexes) < sampleSize:
        set.add(random.randint(0, len(population) - 1))
    newPop = [population[i] for i in indexes]
    return newPop


def sort(pop):
    return sorted(pop, key=lambda x: x.getFitness())

def subSample(pop):
    # gets 4 from the top, 3 from the middle and 3 from the bottom
    #TODO fix this so it isnt shit
    newPopIndex = set()
    newPopIndex.add(0)
    for i in range(3):
        newPopIndex.add(random.randint(1, 30))
        newPopIndex.add(random.randint(31, 60))
        newPopIndex.add(random.randint(61, 99))
    while len(newPopIndex) < 10:
        newPopIndex.add(random.randint(1,99))
    newPop = [pop[i] for i in newPopIndex]
    return newPop