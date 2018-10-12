import genotype
import mutators
import numpy as np
import random
import math


def run(genome, iterations, tempFunction):

    best = current = genome
    temp = 2792964000
    for i in range(iterations):
        new = genotype.genotype(mutators.flipOne(current))
        new.setFitness()
        if accept(current.getFitness(), new.getFitness(), temp):
            current = new
            if current.getFitness() <= best.getFitness():
                best = current
                print(best.getFitness())

        temp = tempFunction(temp)
    return best


def tempDecay(temp):
    return temp*0.92


def accept(current, new, temp):
    if new <= current:
        return True
    else:
        prob = math.exp(-(new-current)/temp)
        #print(new-current,temp,prob)
        return random.random()<prob