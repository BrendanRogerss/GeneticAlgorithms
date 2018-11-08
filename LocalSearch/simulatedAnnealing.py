import genotype
import mutators
import numpy as np
import random
import math
import timeCounter

def run(genome, allotedTime, tempFunction):
    best = current = genome
    temp = findInitTemp()
    timeCounter.start()
    # print(temp)
    while not timeCounter.finished(allotedTime):
        new = mutators.flipOne(current)  # flip random bit

        if accept(current.getFitness(), new.getFitness(), temp):  # check acceptance
            current = new
            if current.getFitness() <= best.getFitness():
                best = current
                print(best.getFitness())
        temp = tempFunction(temp)
    return best


def tempDecay(temp):
    return temp * 0.99


def accept(current, new, temp):
    if new <= current:
        return True
    else:
        prob = math.exp(-(new - current) / temp)
        # print(new-current,temp,prob)
        return random.random() < prob


def findInitTemp():
    solutions = [genotype.genotype() for i in range(100)]
    avg = sum(i.getFitness() for i in solutions) / 100
    temp = 10000000

    while not (0.41 > math.exp(-avg / temp) > 0.39):
        if math.exp(-avg / temp) > 0.41:
            temp /= 2
        elif math.exp(-avg / temp) < 0.39:
            temp += temp / 2
    return temp
