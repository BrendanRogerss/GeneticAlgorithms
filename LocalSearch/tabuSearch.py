import random
import genotype
import mutators
import timeCounter

def run(genome, tenure, time):
    tabu = [0 for i in range(len(genome.getBitString()))] # generate list [0,0,0..,0]
    current = best = genome
    timeCounter.start()
    while not timeCounter.finished(time): # for some numberof times
        neighbours = []
        for j in range(len(tabu)):
            neighbours.append((j,mutators.flipOneAt(current,j))) # store new solution in tuple, (indexFlipped, solution)
        neighbours.sort(key=lambda x: x[1].getFitness()) # sort based on solutions fitness
        index = 0
        for k in range(len(neighbours)): # work out which move is best thats not tabu
            if tabu[neighbours[k][0]] == 0:
                index = k
                break
        if neighbours[0][1].getFitness() < best.getFitness(): # check if we want to violate tabu for best solution
            index = 0
        current = neighbours[index][1]
        tabu = updateTabu(tabu, tenure, neighbours[index][0]) #update taby

        if current.getFitness() < best.getFitness():
            best = current
    return best


def updateTabu(tabu, tenure, change):
    for i in range(len(tabu)):
        if tabu[i] != 0:
            tabu[i] -= 1
    tabu[change] = tenure
    return tabu
