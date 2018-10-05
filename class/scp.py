import numpy as np


def generate_solution_greedy(matrix):
    # define universe
    U = list(range(1,matrix.shpe()[0]))
    solution = np.zeros(matrix.shpe[1])

    while len(U) > 0:
        cheapest_column_index = 0
        cheapest_column_cover = []
        cheapest_column_cost = np.inf

        for i, column in enumerate(matrix.T):
            cost = column[0]
            new_cover = [x for x in np.delete(np.where(column)[0], 0) if x in U]

            length = len(new_cover)
            if length > 0:
                value = cost/length
                if value < cheapest_column_cost:
                    cheapest_column_cost = value
                    cheapest_column_cover = new_cover
                    cheapest_column_index = i

            solution[cheapest_column_index] = 1
            U = [u for u in U if u not in cheapest_column_cover]

    return solution


def find_neighbour(matrix, solution):
    viable = False
    while not viable:
        neighbour = solution.copy()
        index = np.random.randint(0,matrix.shape[0])
        neighbour[index] = not neighbour[index]
        viable = is_viable(matrix, neighbour)
    return neighbour

def accept_probibility(current_cost, neighbour_cost, temp):
    if neighbour_cost < current_cost:
        return True
    else:
        prob = np.exp(-(neighbour_cost-current_cost)/temp)
        return prob



def simmulated_annealing(matrix, solution):
    T = 1

    best_cost = currnet_cost =  solution_cost(matrix,solution)
    current_soluction = solution
    best_solution = solution

    cooling_rate = 0.92
    min_temp = 0.001

    while T > min_temp:
        # pick a random neighbour
        neighbour = find_neighbour(current_soluction)
        neighbour_cost = solution_cost(matrix, neighbour)
        # should we move to this neighbour?
        probibility = accept_probibility(currnet_cost, neighbour_cost, T)
        if probibility >= np.random():
            current_soluction = neighbour
            currnet_cost = neighbour_cost

        if currnet_cost < best_cost:
            best_cost = currnet_cost
            best_solution = current_soluction

        #update/cool the stystem

        T = T * cooling_rate
    return best_solution

def solution_cost(instance, solution):
    #instance = matrix
    return sum(instance[0][i] for i in np.where(solution)[0])

if __name__ == '__main__':
    print("")