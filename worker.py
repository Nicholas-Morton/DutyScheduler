class Worker: 
    def __init__(self):
        self.name = ""
        self.thisWeekGeneral = 0
        self.thisWeekDetail = 0
        self.jobs = []
        self.counts = {
            'east': 0,
            'gcb': 0,
            'second': 0,
            'third': 0,
            'dinner': 0,
            'wakings': 0,
            'setup': 0,
            'cleanup': 0,
            'phones': 0,
            'driver': 0,
            'bcu': 0,
            'totalDetails': 0
        }
        
        self.availability = { 
            'Monday': {}, 
            'Tuesday': {}, 
            'Wednesday': {},
            'Thursday': {}, 
            'Friday': {}
        }

        self.daysWorking = []

        self.isHome = True


