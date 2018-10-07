import genotype
import random


def generatePop(popSize, genoSize):
    pop = []
    for i in range(popSize):
        pop.append(genotype.genotype())
        pop[i].generateBitstring(genoSize)
    return pop

def samplePop(population, sampleSize):
    if population < sampleSize:
        assert "population less than sample size"
    indexes = set()
    while len(indexes)<sampleSize:
        set.add(random.randint(0,len(population)-1))
    newPop = [population[i] for i in indexes]
    return newPop