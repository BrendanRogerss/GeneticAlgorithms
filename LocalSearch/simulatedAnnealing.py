import genotype
import mutators
import numpy as np
import random
import math


def run(genome, iterations, tempFunction):

    best = current = genome
    temp = 2792964000

    for i in range(iterations):
        new = mutators.flipOne(current) # flip random bit

        if accept(current.getFitness(), new.getFitness(), temp): # check acceptance
            current = new
            if current.getFitness() <= best.getFitness():
                best = current

        temp = tempFunction(temp)
    return best


def tempDecay(temp):
    return temp*0.99


def accept(current, new, temp):
    if new <= current:
        return True
    else:
        prob = math.exp(-(new-current)/temp)
        #print(new-current,temp,prob)
        return random.random()<prob