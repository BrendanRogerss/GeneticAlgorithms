import csv

def readSetCover(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        set = list(reader)
    for i in range(len(set)):
        set[i] = float(set[i])
    return set
