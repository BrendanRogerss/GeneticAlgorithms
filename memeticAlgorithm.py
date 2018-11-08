import population
import genotype
import mutators
from random import randint
from LocalSearch import hillClimbing
from multiprocessing import Process
import timeCounter

def memetic(time, popSize=100):
    pop = population.generatePop(popSize)
    pop = population.sort(pop)

    best = pop[0]
    noImprove = 0
    timeCounter.start()
    while not timeCounter.finished(time):
        pop = population.subSample(pop)
        newPop = []
        # while len(newPop) < popSize-len(pop):
        for i in range(popSize-len(pop)):
            # Local Search
            p = Process(target=localSearch, args=(pop, newPop))
            p.start()
            p.join()
            # localSearch(pop,newPop)

        pop = pop+newPop
        pop = population.sort(pop) # sort according to fitness

        if pop[0].getFitness() < best.getFitness(): # check if its the best
            best = pop[0]
            noImprove = 0
            print(pop[0].getFitness(), pop[0].getBitString())
        else:
            noImprove += 1
    return best

def localSearch(pop, newPop):
    newGenome = mutators.onePointCrossover(pop[randint(0, len(pop) - 1)], pop[randint(0, len(pop) - 1)],
                                           randint(0, len(pop[0].getBitString()) - 1))
    newGenome = mutators.mutate(newGenome, 0.05)

    newGenome = hillClimbing.run(newGenome, 100, 0.1)  # local search
    newPop.append(newGenome)  # add to population