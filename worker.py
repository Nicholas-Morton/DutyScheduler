class Worker: 
    def __init__(self):
        self.name = ""
        self.thisWeekGeneral = 0
        self.thisWeekDetail = 0
        self.generalCounts = {
            'east': 0,
            'gcb': 0,
            'second': 0,
            'third': 0,
            'dinner': 0
        }
        self.detailCounts = {
            'wakings': 0,
            'setup': 0,
            'cleanup': 0,
            'phones': 0,
            'driver': 0,
            'bcu': 0,
            'totalDetails': 0
        }
        self.mondayAvailability = {
            'wakings': None,
            'setup': None,
            'cleanup': None,
            'phones': None
        }
        self.tuesdayAvailability = {
            'wakings': None,
            'setup': None,
            'cleanup': None,
            'phones': None
        }
        self.wednesdayAvailability = {
            'wakings': None,
            'setup': None,
            'cleanup': None,
            'phones': None
        }
        self.thursdayAvailability = {
            'wakings': None,
            'setup': None,
            'cleanup': None,
            'phones': None
        }
        self.fridayAvailability = {
            'wakings': None,
            'setup': None,
            'cleanup': None,
            'driver': None
        }
        self.isHome = False

    def print(self):
        print('I\'m a worker, my name is ' + self.name)
