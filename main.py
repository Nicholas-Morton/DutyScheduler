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

# Deprecated

# Fix to make is take in a workerDict and update it with generals
# def getWorkers(fileName): 
#     workerDict = {}

#     with open(fileName, newline='') as f:  # This bit is hardcoded due to the schema of the spreadsheet
#         reader = csv.reader(f)  # Probably should use dictionary reader in this case
#         for row in reader:
#             if row[0] != 'Name': 
#                 newWorker = Worker()
#                 newWorker.name = row[0]  
#                 newWorker.counts['east'] = int(row[1])
#                 newWorker.counts['gcb'] = int(row[2])
#                 newWorker.counts['second'] = int(row[3])
#                 newWorker.counts['third'] = int(row[4])
#                 newWorker.counts['dinner'] = int(row[5])
#                 workerDict.update( {row[0]: newWorker} )
    
#     return workerDict

def getDetailAvailability(workerDict):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

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
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    copyWorkerDict = workerDict.copy()
    weekGroups = []
    
    for day in days:
        group = []
        
        while len(group) < size and len(copyWorkerDict) > 0:
            key = random.choice(list(copyWorkerDict.keys()))
            if copyWorkerDict[key].thisWeekDetail < 4 and copyWorkerDict[key].availability[day][task] == 'yes':
                copyWorkerDict[key].thisWeekDetail += 1  # Should also update the spreadsheet
                group.append(key)
            else: 
                del copyWorkerDict[key]  # Deletes entries to avoid infinate loop if size condition can't be met

        weekGroups.append(group)

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
            'bcu']
    workerDict = getWorkers('Example General_Detail Count.csv', jobs)
    getDetailAvailability(workerDict)

    # for key in list(workerDict.keys()):
    #     print(workerDict[key].availability)


    # getDetailAvailability(workerDict)

    # for key in workerDict: 
    #     for availability in workerDict[key].availability:
            #print(workerDict[key].availability[availability])

    # generalWorkers = getWorkers('Example General_Detail Count.csv')


    # print('Second Floor: ' + str(getGeneralGroup(workerDict, 'second', 4)))
    # print('Third Floor: ' + str(getGeneralGroup(workerDict, 'third', 4)))
    # print('GCB: ' + str(getGeneralGroup(workerDict, 'gcb', 4)))
    # print('Eastside: ' + str(getGeneralGroup(workerDict, 'east', 3)))
    # print('Dinner: ' + str(getGeneralGroup(workerDict, 'dinner', 5)))

    print(getDetailGroups(workerDict, 'wakings', 2))

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