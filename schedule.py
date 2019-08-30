class Schedule:
    def __init__(self, name):
        self.name = name
        self.groups = {
            'Group 1': [], 
            'Group 2': [], 
            'Group 3': [], 
            'Group 4': [], 
            'Group 5': []
        }

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


    def groupsToFormattedCsv(self, writer):
        csvGroups = []

        for group in self.groups:
            csvGroups.append(group)

        for group in csvGroups: 
            csvStr = group + ','
            for person in self.groups[group]:
                csvStr+=person + ','
            writer.writerow(csvStr)
    
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

