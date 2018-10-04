import random

# edits the bitString passed in, also returns it
def mutate(genotype, chance):
    for i in range(len(genotype)):
        if random.random() < chance:
            genotype[i] = not genotype[i]
    return genotype

# deep copy & mutate
def deepMutate(genotype, chance):
    newGenotype = [i for i in genotype]
    return mutate(newGenotype, chance)