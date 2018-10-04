import genotype
import random
import mutators

def run(genome, iterations, chance):
    champ = genome
    for i in range(iterations):
        newBitString = mutators.deepMutate(genome.getBitString(), chance)

        contender = genotype.genotype(newBitString)
        contender.setFitness()
        if contender.getFitness() < champ.getFitness():
            champ = contender

    return champ