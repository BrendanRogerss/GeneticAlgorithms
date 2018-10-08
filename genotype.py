import random
import fitness

def placeHolder(a,b):
    return None


fitnessFunction = placeHolder


class genotype():


    def __init__(self, bitString = None):
        if bitString is not None:
            self.bitString = bitString
        else:
            self.bitString = []
            self.generateBitstring()
        self.setFitness()


    def setFitness(self):
        self.fitness = fitnessFunction(self.bitString)


    def getFitness(self):
        return self.fitness

    def generateBitstring(self):
        for i in range(len(fitness.problem)):
            self.bitString.append(random.randint(0,1))

    def getBitString(self):
        return self.bitString