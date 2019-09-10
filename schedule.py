import csv

class Schedule:
    def __init__(self, name): 
        self.name = name
        self.groups = {} 
        self.details = {} 

    def addGroup(self, task, group):
        self.groups.update( {task: group} )
        
    def addDetail(self, task, group): 
        self.details.update( {task: group} )

    def groupsToFormattedCsv(self):
        csvGroups = []
        csvDetails = []
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for task in self.groups:
            csvGroups.append(task)
        
        for task in self.details:
            csvDetails.append(task)
            
        with open (self.name + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)  # do with dicts

            writer.writerow(['Generals'])

            for task in csvGroups: 
                csvStr = ['', task]
                for person in self.groups[task]:
                    csvStr.append(person)
                writer.writerow(csvStr)
            writer.writerow(['Details'])

            for day in days:
                writer.writerow([day])
                for task in csvDetails:
                    csvStr = ['', task]
                    for person in self.details[task][day]:
                        csvStr.append(person)
                    writer.writerow(csvStr)


