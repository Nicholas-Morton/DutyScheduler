import csv

class Schedule:
    def __init__(self, name, groups, details): 
        self.name = name
        self.groups = {  # Make this groups dict based on a list of group types passed in
            'east': [], 
            'gcb': [], 
            'second': [], 
            'third': [], 
            'dinner': []
        }
        self.details = {} # Make this details dict based on a list of detail types passed in

    def print(self):
        print('I\'m a schedule, my name is ' + self.name)

    def printGroupsCsv(self): 
        csvGroups = []

        for group in self.groups:
            csvGroups.append(group)

        for group in csvGroups: 
            csvStr = group + ','
            for person in self.groups[group]:
                csvStr+=person + ','
            print(csvStr)


    def groupsToFormattedCsv(self, filename):
        csvGroups = []

        for group in self.groups:
            csvGroups.append(group)
        with open (filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)  # do with dicts

            for group in csvGroups: 
                csvStr = [group]
                for person in self.groups[group]:
                    csvStr.append(person)
                writer.writerow(csvStr)
                print(csvStr) 

    
    def detailsToCsv(self, writer):
        print("not implemented")

    def printScheduleOutline(self):
        print("Groups,")
        print(",Group1,")
        print(",Group2,")
        print(",Group3,")
        print(",Group4,")
        print(",Group5,")
        print("Details,")
        print("Monday,Wakings,")
        print(",Lunch Setup,")
        print(",Lunch Cleanup,")
        print(",Phones,")
        print("Tuesday,Wakings,")
        print(",Lunch Setup,")
        print(",Lunch Cleanup,")
        print(",Phones,")
        print("Wednesday,Wakings,")
        print(",Lunch Setup,")
        print(",Lunch Cleanup,")
        print(",Phones,")
        print("Thursday,Wakings,")
        print(",Lunch Setup,")
        print(",Lunch Cleanup,")
        print(",Phones,")
        print("Friday,Wakings,")
        print(",Lunch Setup,")
        print(",Lunch Cleanup,")
        print(",Sober D,")
        print("Saturday,BCU,")
        print(",Wakings,")
        print(",Sober D,")
        print("Sunday,BCU")
        print("Wakings")

