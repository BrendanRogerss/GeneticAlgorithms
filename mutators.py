import random
import genotype

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

def flipOne(genome):
    bitString = genome.getBitString().copy()
    index = random.randint(0,len(bitString)-1)
    bitString[index] = not bitString[index]
    return bitString

def onePointCrossover(genomeA, genomeB, index):
    newBitstring = genomeA.getBitString()[:index]+genomeB.getBitString()[index:]
    return genotype.genotype(newBitstring)