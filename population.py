import genotype

pop = []

def generatePop(popSize, genoSize):
    for i in range(popSize):
        pop.append(genotype.genotype())
        pop[i].generateBitstring(genoSize)
