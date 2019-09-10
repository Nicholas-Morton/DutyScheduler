from schedule import Schedule
from worker import Worker
import csv
import random

def getWorkers(fileName, jobs):
    workerDict = {}

    with open(fileName, newline='') as f:
        fieldNames = ['name','east','gcb','second','third','dinner','wakings','setup','cleanup','phones','driver','bcu']
        reader = csv.DictReader(f, fieldnames=fieldNames)
        next(reader)  
        for row in reader:
            newWorker = Worker()
            newWorker.name = row['name']
            workerDict.update( {row['name']: newWorker} )
            for job in jobs: 
                workerDict[row['name']].counts[job] = int(row[job])

    return workerDict

def getDetailAvailability(workerDict):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for day in days:
        filename = 'availabilities/' + day + '.csv'
        with open(filename, newline='') as f:
            fieldNames = ['name', 'wakings', 'setup', 'cleanup', 'phones']
            reader = csv.DictReader(f, fieldnames=fieldNames)
            next(reader)
            for row in reader:
                for field in fieldNames[1:]:  # Gets rid of the name being inserted into every dict
                    workerDict[row['name']].availability[day].update( {field: row[field]} )

def getGeneralGroup(workerDict, task, size):
    copyWorkerDict = workerDict.copy()
    group = []
    vetNum = 0  # vetNum checks to see who has done a certain task the most 
    allSameNum = 0  # sameNum makes checks to see if everyone has had the same number of duties
                    # so that the vet number isn't accounted for
    
    for worker in copyWorkerDict: 
        if copyWorkerDict[worker].counts[task] >= vetNum:
            vetNum = copyWorkerDict[worker].counts[task]
            allSameNum += 1
    
    if allSameNum == len(list(copyWorkerDict.keys())):
        while len(group) < size and len(copyWorkerDict) > 0:
            key = random.choice(list(copyWorkerDict.keys()))
            if copyWorkerDict[key].thisWeekGeneral < 1:
                copyWorkerDict[key].thisWeekGeneral += 1  # Should also update the spreadsheet
                group.append(key)
            else: 
                del copyWorkerDict[key]  # Deletes entries to avoid infinate loop if size condition can't be met
    
    else: 
        while len(group) < size and len(copyWorkerDict) > 0:
            key = random.choice(list(copyWorkerDict.keys()))
            if copyWorkerDict[key].counts[task] < vetNum and copyWorkerDict[key].thisWeekGeneral < 1:
                copyWorkerDict[key].thisWeekGeneral += 1  # Should also update the spreadsheet
                group.append(key)
            else: 
                del copyWorkerDict[key]

    return group

def getDetailGroups(workerDict, task, size):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # copyWorkerDict = workerDict.copy()
    weekGroups = {}
    
    for day in days:
        group = []
        copyWorkerDict = workerDict.copy()
        while len(group) < size and len(copyWorkerDict) > 0:
            key = random.choice(list(copyWorkerDict.keys()))
            if copyWorkerDict[key].thisWeekDetail < 4 and copyWorkerDict[key].availability[day][task] == ('yes' or 'maybe') and copyWorkerDict[key].jobs.count(task) <= 3:
                copyWorkerDict[key].thisWeekDetail += 1  # Should also update the spreadsheet
                group.append(key)
                copyWorkerDict[key].jobs.append(task)
                del copyWorkerDict[key]

            else: 
                del copyWorkerDict[key]  # Deletes entries to avoid infinate loop if size condition can't be met

        weekGroups.update( {day: group} )

    return weekGroups

def main():
    jobs = ['east', 
            'gcb', 
            'second', 
            'third', 
            'dinner', 
            'wakings',
            'setup',
            'cleanup',
            'phones',
            'driver',
            'bcu']  # Maybe make a new csv file with all of the jobs and the number of people needed
    workerDict = getWorkers('Example General_Detail Count.csv', jobs)

    getDetailAvailability(workerDict)

    newSchedule = Schedule('output')

    newSchedule.addGroup('east', getGeneralGroup(workerDict, 'east', 3))
    newSchedule.addGroup('gcb', getGeneralGroup(workerDict, 'gcb', 4))
    newSchedule.addGroup('second', getGeneralGroup(workerDict, 'second', 4))
    newSchedule.addGroup('third', getGeneralGroup(workerDict, 'third', 4))
    newSchedule.addGroup('dinner', getGeneralGroup(workerDict, 'dinner', 5))

    newSchedule.addDetail('wakings', getDetailGroups(workerDict, 'wakings', 2))
    newSchedule.addDetail('setup', getDetailGroups(workerDict, 'setup', 2))
    newSchedule.addDetail('cleanup', getDetailGroups(workerDict, 'cleanup', 4))
    newSchedule.addDetail('phones', getDetailGroups(workerDict, 'phones', 2))

    newSchedule.groupsToFormattedCsv()

if __name__ == '__main__':
    main()