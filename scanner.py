import csv
import numpy as np
import re

def readShittySetPartitioning(fileName):
    problem = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        set = list(reader)
        for i in set[0]:
            problem.append(float(i))
    return problem

def readNumberPartitioning(fileName):
    problems = []
    lines = [line.strip('\n') for line in open(fileName)]
    #todo: this better
    i = 0
    while i < len(lines):
        instance = []
        if lines[i]=='':
            i+=1

        for j in range(i+1,i+int(lines[i][0:2])+1):
            instance.append(float(lines[j]))
        i+=int(lines[i][0:2])+1
        problems.append(instance)
    return problems



def readSetCover(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        rows, columns = [int(s) for s in line.split(' ') if s.isdigit()]

        matrix = np.empty([rows + 1, columns])
        columnIndex = 0

        while columnIndex < columns:
            line = f.readline()
            for number in map(int, re.findall('\d+', line)):
                matrix[0][columnIndex] = number
                columnIndex += 1
        rowIndex = 1
        for line in f:
            setSize = int(line)
            counter = 0
            while counter < setSize:
                line = f.readline()
                for number in map(int, re.findall('\d+',line)):
                    matrix[rowIndex][number-1] = 1
                    counter += 1

            rowIndex += 1

    return matrix