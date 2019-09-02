from schedule import Schedule
from worker import Worker
import csv
import random

def getWorkerNames(fileName):
    workerDict = {}

    with open(fileName, newline='') as f:
        fieldNames = ['name']
        reader = csv.DictReader(f, fieldnames=fieldNames)
        next(reader)  
        for row in reader:
            newWorker = Worker()
            newWorker.name = row['name']
            workerDict.update( {row['name']: newWorker} )

    return workerDict

# Fix to make is take in a workerDict and update it with generals
def getWorkers(fileName): 
    workerDict = {}

    with open(fileName, newline='') as f:  # This bit is hardcoded due to the schema of the spreadsheet
        reader = csv.reader(f)  # Probably should use dictionary reader in this case
        for row in reader:
            if row[0] != 'Name': 
                newWorker = Worker()
                newWorker.name = row[0]  
                newWorker.generalCounts['east'] = int(row[1])
                newWorker.generalCounts['gcb'] = int(row[2])
                newWorker.generalCounts['second'] = int(row[3])
                newWorker.generalCounts['third'] = int(row[4])
                newWorker.generalCounts['dinner'] = int(row[5])
                workerDict.update( {row[0]: newWorker} )
    
    return workerDict

def getDetailAvailability(workerDict):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    for day in days:
        filename = 'availabilities/' + day + '.csv'
        with open(filename, newline='') as f:
            fieldNames = ['name', 'job1', 'job2', 'job3', 'job4']
            reader = csv.DictReader(f, fieldnames=fieldNames)
            next(reader)
            for row in reader:
                for field in fieldNames[1:]:  # Gets rid of the name being inserted into every dict
                    workerDict[row['name']].availability[day].update( {field: row[field]} )

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

def getDetailGroups(wokerDict, tasks):
    print('Not implemented')

def main():

    workerDict = getWorkerNames('Example General_Detail Count.csv')
    getDetailAvailability(workerDict)

    for key in workerDict: 
        for availability in workerDict[key].availability:
            print(workerDict[key].availability[availability])

    # Make this a test case
    # newSchedule = Schedule('Nicholas')
    # newSchedule.groups['Group 1'] = ['Nic', 'Gaston', 'Preston', 'Kyle']
    # newSchedule.groups['Group 5'] = ['Nathan', 'Noah', 'John', 'Max']
    # newSchedule.printGroupsCsv()

    #########################################################################

    # groups = ['east', 'gcb', 'second', 'third', 'dinner']
    # details = []

    # newSchedule = Schedule('9-2-2019', groups, details)
    # workerDict = getWorkers('Example General_Detail Count.csv')

    # for key in list(newSchedule.groups.keys()):
    #     newSchedule.groups[key] = getGeneralGroup(workerDict, key, 3)
    
    # newSchedule.groupsToFormattedCsv('output.csv')

    # print(newSchedule.groups['east'])

    ##########################################################################

    # print(getGeneralGroup(workerDict, 'east', 4))
    # print(getGeneralGroup(workerDict, 'gcb', 4))
    # print(getGeneralGroup(workerDict, 'second', 4))
    # print(getGeneralGroup(workerDict, 'third', 4))
    # print(getGeneralGroup(workerDict, 'dinner', 3))


if __name__ == '__main__':
    main()