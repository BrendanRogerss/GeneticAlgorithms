import genotype
import random
import mutators

def run(genome, iterations, chance):
    champ = genome
    for i in range(iterations):
        #contender = mutators.deepMutate(genome, chance)
        contender = mutators.flipOne(champ)
        if contender.getFitness() < champ.getFitness():
            champ = contender

    return champ