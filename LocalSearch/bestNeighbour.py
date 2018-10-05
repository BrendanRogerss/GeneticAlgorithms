import genotype


def run(genome):
    for i in range(len(genome.getBitString())):
        bitString = genome.getBitString().copy()
        bitString[i] = not bitString[i]
        newGenome = genotype.genotype(bitString)
        newGenome.setFitness()
        if newGenome.getFitness() < genome.getFitness():
            genome = newGenome
        return genome