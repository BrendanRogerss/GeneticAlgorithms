import random
import genotype
import mutators


def run(genome, tenure, iterations):
    tabu = [0 for i in range(len(genome.getBitString()))]
    current = best = genome
    for i in range(iterations):
        neighbours = []
        for j in range(len(tabu)):
            neighbours.append((j,mutators.flipOneAt(current,j)))
        neighbours.sort(key=lambda x: x[1].getFitness())
        index = 0
        for k in range(len(neighbours)):
            if tabu[neighbours[k][0]] == 0:
                index = k
                break
        if neighbours[0][1].getFitness() < best.getFitness():
            index = 0
        current = neighbours[index][1]
        tabu = updateTabu(tabu, tenure, neighbours[index][0])

        if current.getFitness() < best.getFitness():
            best = current
    return best


def updateTabu(tabu, tenure, change):
    for i in range(len(tabu)):
        if tabu[i] != 0:
            tabu[i] -= 1
    tabu[change] = tenure
    return tabu
