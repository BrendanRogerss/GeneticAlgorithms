import random

class genotype():

    def __init__(self):
        self.bitString = []
        self.fitness = float('inf')

    def setFitness(self, evaluator):
        self.fitness = evaluator(self.bitString)

    def getFitness(self):
        return self.fitness

    def generateBitstring(self,n):
        for i in range(n):
            self.bitString.append(random.randint(0,1))