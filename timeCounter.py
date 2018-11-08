import time

startTime = [0]

def start():
    startTime[0] = time.time()

def finished(allotedTime):
    # alloted is in seconds
    return (time.time()-startTime[0]) > allotedTime