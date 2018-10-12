import genotype
import itertools

# these are mostly for testing

def run(genome):
    best = genome
    # returns the best neighbour
    for i in range(len(genome.getBitString())):
        bitString = genome.getBitString().copy()
        bitString[i] = not bitString[i]
        newGenome = genotype.genotype(bitString)
        newGenome.setFitness()
        if newGenome.getFitness() < genome.getFitness():
            best = newGenome
        return best

#bruteforces all possible solutions
def bruteForce():
    best = genotype.genotype()
    n = len(best.getBitString())
    bitStrings = list(map(list, itertools.product([0, 1], repeat=n)))
    for i in bitStrings:
        new = genotype.genotype(i)
        if new.getFitness() < best.getFitness():
            best = new
    return best