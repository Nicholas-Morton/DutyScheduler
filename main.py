from schedule import Schedule
from worker import Worker

def main():
    newSchedule = Schedule("Nicholas")
    newSchedule.groups["Group 1"] = ["Nic", "Gaston", "Preston", "Kyle"]
    newSchedule.groups["Group 5"] = ["Nathan", "Noah", "John", "Max"]
    newSchedule.printGroupsCsv()
    print("Hello world")

if __name__ == "__main__":
    main()