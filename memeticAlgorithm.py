import population
import genotype
import mutators
from random import randint
from LocalSearch import hillClimbing


def memetic(failureLimit, popSize=100):
    pop = population.generatePop(popSize)
    pop = population.sort(pop)

    best = pop[0]
    noImprove = 0

    while noImprove < failureLimit:
        pop = population.subSample(pop)
        newPop = []
        while len(newPop) < popSize-len(pop):
            # make new genome
            newGenome = mutators.onePointCrossover(pop[randint(0,len(pop) - 1)], pop[randint(0,len(pop) - 1)],
                                                   randint(0, len(pop[0].getBitString()) - 1))
            newGenome = mutators.mutate(newGenome, 0.05)

            newGenome = hillClimbing.run(newGenome,100,0.1) #local search
            newPop.append(newGenome) # add to population
        pop = pop+newPop
        pop = population.sort(pop) # sort according to fitness

        if pop[0].getFitness() < best.getFitness(): # check if its the best
            best = pop[0]
            noImprove = 0
        else:
            noImprove += 1
    return best
