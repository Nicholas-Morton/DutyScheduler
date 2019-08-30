from schedule import Schedule
from worker import Worker
import csv
import random

def getWorkers(fileName): 
    workerDict = {}

    with open(fileName, newline='') as f:  # This bit is hardcoded due to the schema of the spreadsheet
        reader = csv.reader(f)  # Probably should use dictionary reader in this case
        for row in reader:
            if row[0] != "Name": 
                newWorker = Worker()
                newWorker.name = row[0]  
                newWorker.generalCounts["east"] = int(row[1])
                newWorker.generalCounts["gcb"] = int(row[2])
                newWorker.generalCounts["second"] = int(row[3])
                newWorker.generalCounts["third"] = int(row[4])
                newWorker.generalCounts["dinner"] = int(row[5])
                workerDict.update( {row[0]: newWorker} )
  
    return workerDict

def getGeneralGroup(workerDict, task, size):
    group = []
    vetNum = 0  # vetNum checks to see who has done a certain task the most 
    allSameNum = 0  # sameNum makes checks to see if everyone has had the same number of duties
                    # so that the vet number isn't accounted for
    
    for worker in workerDict: 
        if workerDict[worker].generalCounts[task] > vetNum:
            vetNum = worker.generalCounts[task]
            allSameNum += 1
        if workerDict[worker].generalCounts[task] == vetNum: 
            allSameNum += 1
    
    if allSameNum == len(list(workerDict.keys())):
        while len(group) < size:
            key = random.choice(list(workerDict.keys()))
            if workerDict[key].thisWeekGeneral < 1:
                workerDict[key].thisWeekGeneral += 1  # Should also update the spreadsheet
                group.append(key)
    
    else: 
        while len(group) < size:
            key = random.choice(list(workerDict.keys()))
            if workerDict[key].generalCounts[task] < vetNum and workerDict[key].thisWeekGeneral < 1:
                workerDict[key].thisWeekGeneral += 1  # Should also update the spreadsheet
                group.append(key)

    return group

def main():
    # Make this a test case
    # newSchedule = Schedule("Nicholas")
    # newSchedule.groups["Group 1"] = ["Nic", "Gaston", "Preston", "Kyle"]
    # newSchedule.groups["Group 5"] = ["Nathan", "Noah", "John", "Max"]
    # newSchedule.printGroupsCsv()

    workerDict = getWorkers("Example General_Detail Count.csv")
    print(getGeneralGroup(workerDict, "east", 4))
    print(getGeneralGroup(workerDict, "gcb", 4))
    print(getGeneralGroup(workerDict, "second", 4))
    print(getGeneralGroup(workerDict, "third", 4))
    print(getGeneralGroup(workerDict, "dinner", 3))


if __name__ == "__main__":
    main()