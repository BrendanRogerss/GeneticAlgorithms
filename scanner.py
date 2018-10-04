import csv

def readShittySetPartitioning(fileName):
    problem = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        set = list(reader)
        for i in set[0]:
            problem.append(float(i))
    return problem

def readSetPartitioning(fileName):
    problems = []
    lines = [line.strip('\n') for line in open(fileName)]
    #todo: this better
    i = 0
    while i < len(lines):
        instance = []
        if lines[i]=='':
            i+=1
        i
        for j in range(i+1,i+int(lines[i][0:2])+1):
            instance.append(float(lines[j]))
        i+=int(lines[i][0:2])+1
        problems.append(instance)
    return problems