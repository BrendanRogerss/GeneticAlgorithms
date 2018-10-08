import population
import genotype
import mutators
from random import randint
from LocalSearch import hillClimbing


def ga(failureLimit, popSize=100):
    pop = population.generatePop(popSize)
    pop = population.sort(pop)

    best = pop[0]
    noImprove = 0

    while noImprove < failureLimit:
        pop = population.subSample(pop)
        while len(pop) < popSize:
            newGenome = mutators.onePointCrossover(pop[randint(0,len(pop) - 1)], pop[randint(0,len(pop) - 1)],
                                                   randint(0, len(pop[0].getBitString()) - 1))
            newGenome = mutators.mutate(newGenome, 0.05)

            newGenome = hillClimbing.run(newGenome,100,0.1)
            pop.append(newGenome)
        pop = population.sort(pop)

        if pop[0].getFitness() < best.getFitness():
            best = pop[0]
            noImprove = 0
        else:
            noImprove += 1
    return best
