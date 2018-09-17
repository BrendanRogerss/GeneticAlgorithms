import genotype
import fitness
import scanner

mouse = genotype.genotype()
problem = scanner.readSetCover("SetProblems/a.csv")

while mouse.getFitness() != 0:
    mouse = genotype.genotype()
    mouse.generateBitstring()
    mouse.setFitness(fitness.setPartition)
