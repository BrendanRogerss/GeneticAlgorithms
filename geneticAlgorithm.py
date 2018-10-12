import population
import genotype
import mutators
from random import randint


def ga(failureLimit, popSize=100):
    pop = population.generatePop(popSize) # make population
    pop = population.sort(pop) # sort by fitness

    best = pop[0] # best of the pop always index 0 after sort
    noImprove = 0

    while noImprove < failureLimit:
        pop = population.subSample(pop) # get new pop
        newPop = []
        while len(newPop) < popSize-len(pop):
            newGenome = mutators.onePointCrossover(pop[randint(0,len(pop) - 1)], pop[randint(0,len(pop) - 1)],
                                                   randint(0, len(pop[0].getBitString()) - 1)) # randomly pick parents for new solution
            newGenome = mutators.mutate(newGenome, 0.05) # mutate
            newPop.append(newGenome) # add to population
        pop = newPop+pop
        pop = population.sort(pop)

        if pop[0].getFitness() < best.getFitness(): # check for new best solution
            best = pop[0]
            noImprove = 0
        else:
            noImprove += 1
    return best
