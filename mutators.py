import random
import genotype

# edits the bitString passed in, also returns it
def mutate(genome, chance):
    newGenome = genome.getBitString()
    for i in range(len(newGenome)):
        if random.random() < chance:
            newGenome[i] = not newGenome[i]
    return genotype.genotype(newGenome)

# deep copy & mutate
def deepMutate(genome, chance):
    newGenotype = genotype.genotype(genome.getBitString().copy())
    return mutate(newGenotype, chance)

def flipOne(genome):
    bitString = genome.getBitString().copy()
    index = random.randint(0,len(bitString)-1)
    bitString[index] = not bitString[index]
    return bitString

def onePointCrossover(genomeA, genomeB, index):
    newBitstring = genomeA.getBitString()[:index]+genomeB.getBitString()[index:]
    return genotype.genotype(newBitstring)